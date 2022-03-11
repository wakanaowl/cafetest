import pyodbc

driver = '{ODBC Driver 17 for SQL Server}'
server = 'khan-sql-server.database.windows.net'
database = 'khan-sql-database-02'
username = 'khansqlsever'
password = 'aH9kRZur'

# def __init__(self, driver, host, dbname, user, password):
#     '''
#     DBの接続情報を保持する
#     Parameters
#     ----------
#     host : str
#          ホスト名
#     dbname : str
#         DB名
#     user : str
#         ユーザー名
#     password : str
#         パスワード
#     port : integer
#         ポート
#     '''
#     self.driver = driver
#     self.host = host
#     self.dbname = dbname
#     self.user = user
#     self.password = password



def insert_users(self, userid, username):
    '''
    SQLを実行し、結果を取得する
    Parameters
    ----------
    columns : str
        実行したいSQL
    '''

    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users VALUES ('{}','{}')".format(userid, username))
    conn.commit()
    cur.close()
    conn.close()


def test_json(jsondata):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users VALUES ('{}','{}')".format(jsondata["uid"], jsondata["name"]))
    conn.commit()
    cur.close()
    conn.close()