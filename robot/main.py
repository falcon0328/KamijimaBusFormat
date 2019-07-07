# -*- coding: utf-8 -*-
import sys
import os
from gtfs import gtfs_file as gtfs
from gtfs import gtfs_request_params as request_params
from connection import connection as connection


def print_message(message):
    print("=== " + message + " ===")


def print_error_message(message):
    print("XXX " + message + " XXX")


if __name__ == "__main__":
    # GTFSのファイルを管理するクラス
    gtfs = gtfs.gtfs_file()
    # サーバ接続用インスタンス
    connection = connection.connection()

    print_message("GTFSフォーマットに必要なファイルを確認します")
    if not gtfs.is_exist_files():
        print_error_message("必要なファイルが存在しません")

    print_message("GTFSに必要なファイルの情報をサーバに送信する")
    gtfs_files = gtfs.get_gtfs_files()
    if gtfs_files == []:
        print_error_message("必要なファイルが存在しません")
    for data in gtfs.get_gtfs_files():
        request_params.RequestParams.create_params(data=data)
