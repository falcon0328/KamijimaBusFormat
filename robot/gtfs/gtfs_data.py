class gtfs_data:
    # 拡張子も含めたファイル名
    filename = None
    # ファイルのパス
    filepath = None

    def __init__(self, filename, filepath):
        self.filename = filename
        self.filepath = filepath
