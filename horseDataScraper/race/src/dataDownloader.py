import os, glob, json
from time import sleep
from race.src.my_lib import raceDateGetter
from race.src.my_lib import raceDataGetter
from datetime import datetime
from tqdm import tqdm

import race.src.setting_env

def data_downloader(is_test, is_dry_run):
    IS_TEST = is_test
    IS_DRY_RUN = is_dry_run
    NOW = datetime.now().strftime('%Y-%m-%d-%H-%M')
    mount_point = os.environ["MOUNT_POINT"]
    if IS_TEST:
        data_dir = os.path.join(mount_point, "test/data/race")
        log_dir = os.path.join(mount_point,"test/data/race/log")
    else:
        data_dir = os.path.join(mount_point,"data/race")
        log_dir = os.path.join(mount_point,"data/race/log")

    date_list = glob.glob(os.path.join(data_dir, "*", "*", "*"))
    download_path_list = []
    for date in date_list:
        if len((glob.glob(os.path.join(date, "*")))) == 0:
            download_path_list.append(date)
    try:
        gotten_raceid_list = []
        for path in download_path_list:
            race_date = "".join(path.split(os.sep)[-3:])
            race_ids = raceDateGetter.raceListGetter(race_date)
            htmls = []
            # 全てメモリに格納
            for race_id in tqdm(race_ids):
                # raceを取得して保存
                htmls.append(raceDataGetter.getRaceHtml(race_id))
                sleep(1)
            # 問題なく取得されたら、ドライブに保存
            for race_id, html in zip(race_ids, htmls):
                gotten_raceid_list.append(race_id)
                with open(os.path.join(path, race_id+".html"), "w") as f:
                    if not IS_DRY_RUN:
                        f.write(html)
                    else:
                        pass
            print("-------save {}---------".format(path))
    except Exception as e:
        print(e)
    finally:
        if len(gotten_raceid_list) > 0:
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            with open(os.path.join(log_dir, NOW+".log"), "w") as f:
                d = {
                    "gotten_data": gotten_raceid_list
                }
                if not IS_DRY_RUN:
                    json.dump(d, f, indent=4)
                else:
                    pass
    return gotten_raceid_list

if __name__ == "__main__":
    IS_TEST = race.src.setting_env.IS_TEST
    IS_DRY_RUN = race.src.setting_env.IS_DRY_RUN
    data_downloader(is_test=IS_TEST, is_dry_run=IS_TEST)