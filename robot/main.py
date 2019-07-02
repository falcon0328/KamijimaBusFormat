import sys
import os
from gtfs import gtfs_file


def print_message(message):
    print("=== " + message + " ===")


def print_error_message(message):
    print("XXX " + message + " XXX")


if __name__ == "__main__":
    gtfs = gtfs_file.gtfs_file()

    print_message("GTFSフォーマットに必要なファイルを確認します")
    if not gtfs.is_exist_files():
        print_error_message("必要なファイルが存在しません")

    print_message("GTFSに必要なファイルの情報をサーバに送信する")
    gtfs_files = gtfs.get_gtfs_files()
    if gtfs_files == []:
        print_error_message("必要なファイルが存在しません")
    for filename in gtfs.get_gtfs_files():
        print(filename)
