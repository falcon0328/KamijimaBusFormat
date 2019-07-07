import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from gtfs import gtfs_request_params as request_params


class connection:
    '''
    サーバに接続を行い、データを送信する
    今回はFirebaseに接続して、データを送受信する
    '''
    # Use a service account
    cred = None
    # Firestore
    db = None

    def __init__(self, cred_file_path='./setouchinorikae-firebase-adminsdk-qvzo7-4d9cef8686.json'):
        self.cred = credentials.Certificate(cred_file_path)
        # Firebaseのアプリケーションとして初期化
        firebase_admin.initialize_app(self.cred)
        # Firestoreに接続
        self.db = firestore.client()

    def send(self, params: dict):
        """指定されたパラメータをサーバに送信する

        Arguments:
            params {dict} -- 送信したいデータ
        """
        for key in params.keys():
            for value in params[key]:
                self.db.collection(key).document().set(value)
