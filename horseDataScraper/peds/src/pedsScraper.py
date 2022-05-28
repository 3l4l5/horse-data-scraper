from signal import pthread_sigmask
import socket
import os
import glob
import json
from bs4 import BeautifulSoup
import re
from tqdm import  tqdm
import requests
import time
from datetime import datetime

def getPedsHtml(horse_id):
    PEDS_URL = "https://db.netkeiba.com/horse/ped/{}/"
    url = PEDS_URL.format(horse_id)
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    return response.text

if __name__ == "__main__":
    IS_TEST = True
    NOW = datetime.now().strftime('%Y-%m-%d-%H-%M')
    MOUNT_POINT = os.environ["MOUNT_POINT"]

    if not IS_TEST:
        race_dir = os.path.join(MOUNT_POINT, "data", "race")
        horse_dir = os.path.join(MOUNT_POINT, "data", "horse")
        peds_dir = os.path.join(MOUNT_POINT, "data", "peds")
    else:
        race_dir = os.path.join(MOUNT_POINT, "test", "data", "race")
        horse_dir = os.path.join(MOUNT_POINT, "test", "data", "horse")
        peds_dir = os.path.join(MOUNT_POINT, "test", "data", "peds")

    horse_dirs = glob.glob(os.path.join(horse_dir, "data", "*"))
    peds_dirs = glob.glob(os.path.join(peds_dir, "*"))

    # horseを取得している者の中から、pedsで取得できていないものを抽出
    all_horse_ids_set = set([os.path.basename(path) for path in horse_dirs])
    already_get_horse_ids_set = set([os.path.basename(path) for path in peds_dirs])
    get_id_list = list(all_horse_ids_set - already_get_horse_ids_set)
    for horse_id in tqdm(get_id_list):
        peds_html = getPedsHtml(horse_id)
        time.sleep(1)
        with open(os.path.join(peds_dir, horse_id+".html"), "w") as f:
            f.write(peds_html)