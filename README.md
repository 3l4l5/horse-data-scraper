# horse-data-scraper

## 概要

競馬のhtmlを定期的に取得するスクリプト。dockerコンテナ上で動作します。

## 環境構築

### インストール等

docker がインストールされていれば動作します。するはず。

### 環境変数

環境変数で保存先および通知するSlackのwebhock urlを設定しています。
本プロジェクトでは、環境変数は.envに記載して管理しており、.envを以下のように記載して保存することで環境変数を反映させることができます。

```.env
MOUNT_POINT=<Directories you want to save files>
SLACK_URL=<Your Slack webhook url>
```

## deploy

以下コマンドを実行することで、rootディレクトリに/project/horse-data-scraper/を作成し、このファイルをコピーします。

```bash
sudo bash deploy.sh
```

## 実行方法

以下のコマンドを実行することで、その月のraceデータを一括で取得し、環境変数で指定されている保存先に保存されます。

```bash
bash docker_run.sh
```
