import raceDirMaker
import dataDownloader
import setting_env

IS_TEST = setting_env.IS_TEST
IS_DRY_RUN = setting_env.IS_DRY_RUN

def save_racedata_thismonth(is_test, is_dry_run):
    raceDirMaker.make_dir_this_month(is_test, is_dry_run)
    dataDownloader.data_downloader(is_test, is_dry_run)

if __name__ == "__main__":
    save_racedata_thismonth(is_test=IS_TEST, is_dry_run=IS_DRY_RUN)