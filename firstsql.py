import pyodbc
server = 'khan-sql-server.database.windows.net'
database = 'khan-sql-database-02'
username = 'khansqlsever'
password = '{aH9kRZur}'
driver = '{ODBC Driver 17 for SQL Server}'


# with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
#     with conn.cursor() as cursor:
#         cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
#         row = cursor.fetchone()
#         while row:
#             print(str(row[0]) + " " + str(row[1]))
#             row = cursor.fetchone()

# Sample insert query
# count = cursor.execute(
#     "INSERT INTO users (uid, name) VALUES ('12346','wakana')")
# cnxn.commit()
# print('Rows inserted: ' + str(count))

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
    with conn.cursor() as cursor:
        count = cursor.execute("INSERT INTO users (uid, name) VALUES ('12350','青空カフェ')")
        conn.commit()
        cursor.execute("SELECT TOP (1000) * FROM [dbo].[users]")
        row = cursor.fetchone()
        while row:
            print(row[0] + " " + row[1])
            row = cursor.fetchone()