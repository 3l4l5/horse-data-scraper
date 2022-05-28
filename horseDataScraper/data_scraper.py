from horse.src import autoHorseScraper
from race.src import autoRaceScraper
from peds.src import autoPedsScraper

if __name__ == "__main__":
    print("scraping race html")
    autoRaceScraper.race_scraper(is_test=True, is_dry_run=False)
    print("scraping horse html")
    autoHorseScraper.horse_scraper(is_test=True, is_dry_run=False)
    print("scraping peds html")
    autoPedsScraper.peds_scraper(is_test=True, is_dry_run=False)
