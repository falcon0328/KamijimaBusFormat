#!/bin/bash

# ファイルのコピー
cp ./static/* ./output
# カレントディレクトリの変更
cd ./output
# outputディレクトリに予め存在するzipファイルを削除する
rm *.zip
# ファイルの拡張子一括変更
for filename in *.csv; do mv $filename ${filename%.csv}.txt; done
# zipファイルの作成
zip -r `date "+%Y%m%d%H%M%S"`.zip .
# テキストファイルの一括削除
rm *.txt