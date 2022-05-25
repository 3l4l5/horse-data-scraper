import os
import glob
import json
from bs4 import BeautifulSoup
import re
from tqdm import  tqdm
import requests
import time
from datetime import datetime

def getHorseHtml(horse_id):
    HORSE_URL = "https://db.netkeiba.com/horse/{}/"
    url = HORSE_URL.format(horse_id)
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    return response.text

if __name__ == "__main__":
    MOUNT_POINT = os.environ["MOUNT_POINT"]
    NOW = datetime.now().strftime('%Y-%m-%d-%H-%M')

    race_dir = os.path.join(MOUNT_POINT, "data", "race")
    horse_dir = os.path.join(MOUNT_POINT, "data", "horse")

    log_dir = os.path.join(race_dir, "log")
    data_dirs = list(set(glob.glob(os.path.join(race_dir, "*"))) - set([log_dir]))
    race_logs_path = glob.glob(os.path.join(log_dir, "*"))
    # キーをrace_id,
    horse_id_dict = {}

    horse_log_filename_list = [os.path.basename(path) for path in glob.glob(os.path.join(horse_dir, "log", "*"))]
    # 各logファイルに対して出場馬を取得
    for race_log_path in race_logs_path:
        # 新しく取得されたrace_idについて
        if not os.path.basename(race_log_path) in horse_log_filename_list:
            with open(race_log_path, "r") as f:
                log = json.load(f)
                target_race_ids = log["gotten_data"]
            race_html_paths = []
            for data_dir in data_dirs:
                race_html_paths += glob.glob(os.path.join(data_dir, "*", "*", "*.html"))
            target_html_paths = [path for path in race_html_paths if os.path.basename(path).split(".")[0] in target_race_ids]

            horse_id_list = []
            for target_html_path in tqdm(target_html_paths):
                print(target_html_path)
                with open(target_html_path, "r") as f:
                    html_text = f.read()
                soup = BeautifulSoup(html_text, features="lxml")
                tr_list = soup.find(class_="race_table_01").find_all("tr")
                a_list = []
                for tr in tr_list:
                    a_list += tr.find_all("a")
                pattern =  '(?<=/horse/)\d+?(?=/)'
                for a in a_list:
                    horse_id = re.findall(pattern, a.get("href"))
                    if horse_id:
                        horse_id_list.append(horse_id[0])
            horse_data_dir = os.path.join(horse_dir, "data")
            horse_id_dict[race_log_path] = horse_id_list

    scrape_horse_id_list = []
    for race_log_path in horse_id_dict:
        print("scraping {} now".format(race_log_path))
        for horse_id in tqdm(list(set(horse_id_dict[race_log_path]))):
            horse_html = getHorseHtml(horse_id)
            time.sleep(1)
            os.makedirs(os.path.join(horse_dir, "data", horse_id), exist_ok=True)
            with open(os.path.join(horse_dir, "data", horse_id,  NOW+".html"), "w") as f:
                f.write(horse_html)
            scrape_horse_id_list.append(horse_id)

        # horselogファイルの作成
        log_dir_split = race_log_path.split(os.sep)
        log_dir_split[-3] = "horse"
        horse_log_dir = "/".join(log_dir_split)
        with open(horse_log_dir, "w") as f:
            json.dump({"horse_id": scrape_horse_id_list}, f, indent=4)
