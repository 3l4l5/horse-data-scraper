import requests
from bs4 import BeautifulSoup

def getRaceHtml(race_id):
    base_url = "https://db.netkeiba.com/race/"
    url = base_url + race_id
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    return response.text
