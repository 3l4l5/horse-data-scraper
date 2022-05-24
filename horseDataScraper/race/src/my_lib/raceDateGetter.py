import requests
from bs4 import BeautifulSoup

def getRaceDate(year, month):
    """年月を指定して、その中のレースの行われた日にちを取得する

    Args:
        year (int): 年を指定
        month (int)): 月を指定

    Returns:
        list: レースの開催日を返す
    """
    s_year = str(year)
    s_month = str(month)
    base_url = "https://db.netkeiba.com/"
    url = base_url + "/?pid=race_kaisai&syusai=10&date={}".format(s_year+s_month.zfill(2)+"01")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    calendar = soup.find(class_="race_calendar")
    race_date_list = []
    for td in calendar.find_all("td"):
        if not (td.get("class") is None):
            if td.get("class")[0] == "sun" or td.get("class")[0] == "sat" or td.get("class")[0] == "selected":
                if  not (td.find("a") is None):
                    race_date_list.append(td.find("a").get("href").split("/")[-2])
    return race_date_list

def raceListGetter(date):
    """日付指定でその日に行われたレースを返す関数

    Args:
        date (str): 2021年11月4日なら20211104
    Returns:
        list: その日行われたレースIDのリスト
    """
    race_id_list = []
    base_url = "https://db.netkeiba.com/race/list/"
    url = base_url + date
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for race_top_data in soup.find_all(class_="race_top_data_info"):
        race_id_list.append(race_top_data.find("a").get("href").split("/")[-2])
    return race_id_list


if __name__ == "__main__":
    date_list = getRaceDate(year=2012, month=1)
    race_id_list = raceListGetter(date=date_list[4])
    print(len(race_id_list))

