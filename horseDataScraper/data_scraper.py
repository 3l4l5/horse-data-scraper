from horse.src import autoHorseScraper
from race.src import autoRaceScraper
from peds.src import autoPedsScraper

IS_TEST = True
IS_DRY_RUN = False

if __name__ == "__main__":
    print("scraping race html")
    autoRaceScraper.race_scraper(is_test=IS_TEST, is_dry_run=IS_DRY_RUN)
    print("scraping horse html")
    autoHorseScraper.horse_scraper(is_test=IS_TEST, is_dry_run=IS_DRY_RUN)
    print("scraping peds html")
    autoPedsScraper.peds_scraper(is_test=IS_TEST, is_dry_run=IS_DRY_RUN)
