# Data downloader

データをダウンロードするプロジェクト

1. レースの開催された日にちを取得して、その日にちの名前のフォルダを作成する。(raceDirMaker.py)
2. 作成されているフォルダの中から、中身のからのフォルダを見つけてその日に開催されたレースの生HTMLを作成する(dataDownLoader.py)

## raceDirMaker.py

レースが開催された日にちを取得し、ディレクトリを作成するプログラム。
期間を指定して開催された日を指定する。
コマンド例（2020年1月から、2021年4月までの開催された日にちを取得）
```
python3 raceDirMaker.py year=2020 --month(-m)=1 --year2(-y2)=2021 --month2(-m2)=4
```

コマンド例（2020年3月から、2020年12月までの開催された日にちを取得）
```
python3 raceDirMaker.py year=2020 --month(-m)=3
```

## dataDownloader.py

raceDirMaker.pyで作成されたディレクトリの中を全て見て、空のフォルダを見つけてそのpathが示す日に開催されたレースを取得する。

## テストと切り替え

同ディレクトリ内のIS_TESTをIS_PRODに変更することで開発環境と実行環境を変更することができる（保存先が変わる）

## デプロイ方法

```shell
mv horse/ /horse
```
でルートディレクトリにhorseを移動させ、
horse/data_downloader/race/bin/deploy.sh
を実行しDockedr imageを作成
その後、
horse/bin/autoRaceScraper.sh
を実行することで、今月の今日までのレースを取得する処理を行う。
