import os
import glob


class gtfs_file:
    __gtfs_needs_files = []

    def __init__(self, gtfs_needs_files=["agency",
                                         "calendar",
                                         "fare_attributes",
                                         "feed_info",
                                         "routes",
                                         "stop_times",
                                         "stops",
                                         "trips"]):
        self.__gtfs_needs_files = gtfs_needs_files

    def is_exist_files(self, files=os.listdir("../static/"), path="../static/", ext=".csv"):
        '''
        GTFSのフォーマットに必要なファイルが全て存在するかを確認する
        '''
        for gtfs_file in self.__gtfs_needs_files:
            filename = path + gtfs_file + ext
            print(filename)
            if os.path.isfile(filename) == False:
                return False
        return True

    def get_gtfs_files(self, files=os.listdir("../static/"), path="../static/", ext=".csv"):
        '''
        GTFSのフォーマットに必要なファイルのみを指定したディレクトリから取得する
        '''
        gtfs_files = []
        for gtfs_file in self.__gtfs_needs_files:
            filename = path + gtfs_file + ext
            if os.path.isfile(filename) == False:
                continue
            gtfs_files.append(filename)
        return gtfs_files
