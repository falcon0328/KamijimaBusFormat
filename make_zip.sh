#!/bin/bash
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
# gh-pagesブランチにチェックアウト
git checkout gh-pages
if [ -e ./GTFS ]; then
    # GTFS内にprevディレクトリがなければ
    if [ ! -e ./GTFS/prev ]; then
        # prevディレクトリを作成する
        mkdir ./GTFS/prev
    fi
    # GTFSディレクトリ内にzipファイルが存在すれば
    if [ -e ./GTFS/*.zip ]; then
        # prevディレクトリに移動する
        mv ./GTFS/*.zip ./GTFS/prev/
    fi
else
    # 存在しない場合
    mkdir GTFS
fi
# 今回の成果物であるzipファイルをGTFSディレクトリにコピー
cp ./output/*.zip ./GTFS
# gh-pagesへpush
git add ./GTFS
git commit -m "add GTFS.zip"
git push origin gh-pages
# masterブランチに切り替える
git checkout master