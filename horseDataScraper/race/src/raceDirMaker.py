# 年月を指定して、その年月にレースが開催された日を取得し、日にちのフォルダを作成する
from datetime import datetime
import os
import my_lib.raceDateGetter as raceDateGetter
import argparse
import time
import sys
sys.path.append("../../..")


def makeDateList(year1, year2, month1, month2):
    if year2:
        if year1 >= year2:
            raise ValueError("year2 must be bigger than year1")
        get_year_list = [y for y in range(year1, year2+1)]
    else :
        get_year_list = [year1]

    if month1 and (month2 is None):
        yearmonth = [(str(get_year_list[0]), str(m).zfill(2)) for m in range(month1, 13)]
        if len(get_year_list)>1:
            for y in get_year_list[1:]:
                for m in range(1, 13):
                    yearmonth.append((str(y), str(m).zfill(2)))
    elif month1 and month2:
        if month1 >=  month2:
            raise ValueError("month2 must be bigger than month1")
        if len(get_year_list)>1:
            yearmonth = [(str(get_year_list[0]), str(m).zfill(2)) for m in range(month1, 13)]
            for y in get_year_list[1:-1]:
                for m in range(1, 13):
                    yearmonth.append((str(y), str(m).zfill(2)))
            for m in range(1, month2 + 1):
                yearmonth.append((str(y+1), str(m).zfill(2)))
        elif len(get_year_list)==1:
            yearmonth = [(str(get_year_list[0]), str(m).zfill(2)) for m in range(month1, month2+1)]

    elif month2 and (month1 is None):
        yearmonth = []
        if len(get_year_list)==1:
            yearmonth = [(str(get_year_list[0]), str(m).zfill(2)) for m in range(1, month2)]
        elif len(get_year_list)>1:
            for y in get_year_list[:-1]:
                for m in range(1, 13):
                    yearmonth.append((str(y), str(m).zfill(2)))
            for m in range(1, month2 + 1):
                yearmonth.append((str(y+1), str(m).zfill(2)))
    else:
        yearmonth = []
        for y in get_year_list:
            for m in range(1, 13):
                yearmonth.append((str(y), str(m).zfill(2)))

    return yearmonth

def make_date_dir(path):
    pass

if __name__ == "__main__":
    IS_TEST = False
    IS_DRY_RUN = True

    parser = argparse.ArgumentParser(description='期間を指定してレースの開催日に基づくディレクトリを作成する')
    # 3. parser.add_argumentで受け取る引数を追加していく
    parser.add_argument('-y1', '--year1', type=int, help='取得したい年')    # 必須の引数を追加
    parser.add_argument('-m1', '--month1', type=int, help='取得したい月（指定のない場合、一年間のデータを取得する）')
    parser.add_argument('-y2', '--year2', type=int, help='複数年の取得を行いたい場合は終わりの年')
    parser.add_argument('-m2', '--month2', type=int, help='複数月取得したい場合は終わりの月')
    args = parser.parse_args()
    if args.year1 is None and args.year2 is None and args.month1 is None and args.month2 is None:
        today = datetime.now()
        yearmonth = [(str(today.year), str(today.month))]
    else:
        yearmonth = makeDateList(year1=args.year1, year2=args.year2, month1=args.month1, month2=args.month2)
    if IS_TEST:
        save_dir = "test/data/race"
        log_dir = "test/data/race/log"
    else:
        save_dir = "data/race"
        log_dir = "data/race/log"
    for y, m in yearmonth:
        date_list = raceDateGetter.getRaceDate(year=y, month=m)
        for date in date_list:
            dir_path = os.path.join(save_dir, date[:4], date[4:6], date[6:8])
            print(dir_path)

            #TODO: ファイル保存部分は後に変更予定
            make_date_dir(dir_path)


        time.sleep(1)
