# server = 'khan-sql-server.database.windows.net'
# database = 'khan-sql-database-02'
# username = 'khansqlsever'
# password = 'aH9kRZur'
# driver = '{ODBC Driver 17 for SQL Server}'

import pyodbc


class SQLServerConnect:

    def __init__(self, driver, host, dbname, user, password):
        '''
        DBの接続情報を保持する
        Parameters
        ----------
        host : str
             ホスト名
        dbname : str
            DB名
        user : str
            ユーザー名
        password : str
            パスワード
        port : integer
            ポート
        '''
        self.driver = driver
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

    def __connect(self):
        return pyodbc.connect("DRIVER={};SERVER={};PORT=1433;DATABASE={};UID={};PWD={}".format(self.driver, self.host, self.dbname, self.user, self.password))

    def execute(self, userid, username):
        '''
        SQLを実行し、結果を取得する
        Parameters
        ----------
        columns : str
            実行したいSQL
        '''

        conn = self.__connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users VALUES ('{}','{}')".format(userid, username))
        conn.commit()
        cur.close()
        conn.close()


testsql = SQLServerConnect('{ODBC Driver 17 for SQL Server}',
                           'tcp:khan-sql-server.database.windows.net', 'khan-sql-database-02', 'khansqlsever', 'aH9kRZur')

testsql.execute('13478', '03 slow cafe')