from horse.src import autoHorseScraper
from race.src import autoRaceScraper
from peds.src import autoPedsScraper
import requests
import os

IS_TEST = False
IS_DRY_RUN = False


def slack_notifier(text):
    slack_url = os.environ["SLACK_URL"]
    request_body = {
        "text": text
    }
    request_header = {
        'content-type': 'application/json'
    }

    return requests.post(slack_url, headers=request_header, json=request_body)


if __name__ == "__main__":

    try:
        print("scraping race html")
        get_race_id_list = autoRaceScraper.race_scraper(is_test=IS_TEST, is_dry_run=IS_DRY_RUN)

        race_scrape_result_text = """
        レースデータのスクレイピングを行いました。
        今回スクレイピングした件数は{}件です。
        """.format(len(get_race_id_list))

        slack_notifier(race_scrape_result_text)

        print("scraping horse html")
        get_horse_id_list = autoHorseScraper.horse_scraper(is_test=IS_TEST, is_dry_run=IS_DRY_RUN)

        horse_scrape_result_text = """
        馬の戦績データのスクレイピングを行いました。
        今回スクレイピングした件数は{}件です。
        """.format(len(get_horse_id_list))

        slack_notifier(horse_scrape_result_text)

        print("scraping peds html")
        get_peds_id_list = autoPedsScraper.peds_scraper(is_test=IS_TEST, is_dry_run=IS_DRY_RUN)

        peds_scrape_result_text = """
        馬の血統データのスクレイピングを行いました。
        今回スクレイピングした件数は{}件です。
        """.format(len(get_peds_id_list))

        slack_notifier(peds_scrape_result_text)

    except Exception as e:
        except_text = """
        処理が正しく終了しませんでした。
        エラー内容は以下です
        {}
        """.format(e)
        slack_notifier(except_text)
