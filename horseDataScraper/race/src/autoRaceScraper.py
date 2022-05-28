import race.src.raceDirMaker as raceDirMaker
import race.src.dataDownloader as dataDownloader
import race.src.setting_env as setting_env

IS_TEST = setting_env.IS_TEST
IS_DRY_RUN = setting_env.IS_DRY_RUN

def race_scraper(is_test, is_dry_run):
    raceDirMaker.make_dir_this_month(is_test, is_dry_run)
    dataDownloader.data_downloader(is_test, is_dry_run)

if __name__ == "__main__":
    race_scraper(is_test=IS_TEST, is_dry_run=IS_DRY_RUN)