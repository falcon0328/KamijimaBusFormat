#!/bin/bash

# gh-pagesのブランチに切り替える
git checkout gh-pages
if [ -e ./output ]; then
    # outputディレクトリに予め存在するzipファイルを削除する
    rm ./output/*.zip
else
    # 存在しない場合
    mkdir output
fi
# ファイルのコピー
cp ./static/* ./output
# カレントディレクトリの変更
cd ./output
# ファイルの拡張子一括変更
for filename in *.csv; do mv $filename ${filename%.csv}.txt; done
# zipファイルの作成
zip -r `date "+%Y%m%d%H%M%S"`.zip .
# テキストファイルの一括削除
rm *.txt
# カレントディレクトリを戻す
cd ..
if [ ! -e ./GTFS ]; then
    # 存在しない場合
    mkdir GTFS
fi
# 成果物のzipファイルをGTFSディレクトリにコピー
cp ./output/*.zip ./GTFS
# gh-pagesへpush
git add
git commit -m "add GTFS.zip"
git push origin
# masterブランチに切り替える
git checkout master