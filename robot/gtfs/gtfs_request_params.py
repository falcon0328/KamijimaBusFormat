import pandas as pd
from gtfs import gtfs_data


class RequestParams:
    @staticmethod
    def create_params(data: gtfs_data.gtfs_data):
        '''
        ファイル内容を読み、ヘッダーに付与されている名前と各業の値をもとにサーバに送信する辞書型データを生成する
        :rtype: object
        '''
        data_list = []
        # ファイルを読む
        csv = pd.read_csv(data.filepath)
        # キー値の数だけループ
        for index, row in csv.iterrows():
            params = {}
            for key in csv.keys():
                params[key] = row[key]
            data_list.append(params)
        requestParams = {data.filename: data_list}
        return requestParams
