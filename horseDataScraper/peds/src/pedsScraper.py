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
    NOW = datetime.now().strftime('%Y-%m-%d-%H-%M')
    if os.path.exists(os.path.join("..", "IS_TEST")):
        race_dir = os.path.join("..", "test", "data")
        os.makedirs(race_dir, exist_ok=True)
    elif os.path.exists(os.path.join("..", "IS_PROD")):
        host = socket.gethostname()
        if "Mac" in host:
            race_dir = os.path.join(os.environ['HOME'], "nas", "project", "horse", "data", "race")
            horse_dir = os.path.join(os.environ['HOME'], "nas", "project", "horse", "data", "horse")
            peds_dir = os.path.join(os.environ['HOME'], "nas", "project", "horse", "data", "peds")
        else:
            race_dir = os.path.join("/nas", "project", "horse", "data", "race")
            horse_dir = os.path.join("/nas", "project", "horse", "data", "horse")
            peds_dir = os.path.join("/nas", "project", "horse", "data", "peds")

    horse_dirs = glob.glob(os.path.join(horse_dir, "data", "*"))
    peds_dirs = glob.glob(os.path.join(peds_dir, "*"))

    # horseを取得している者の中から、pedsで取得できていないものを抽出
    get_id_list = list(set([os.path.basename(path) for path in horse_dirs])-set([os.path.basename(path) for path in peds_dirs]))
    for horse_id in tqdm(get_id_list):
        peds_html = getPedsHtml(horse_id)
        time.sleep(1)
        with open(os.path.join(peds_dir, horse_id+".html"), "w") as f:
            f.write(peds_html)