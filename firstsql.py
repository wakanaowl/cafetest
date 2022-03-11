import pyodbc

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
    with conn.cursor() as cursor:
        count = cursor.execute("INSERT INTO users (uid, name) VALUES ('12350','青空カフェ')")
        conn.commit()
        cursor.execute("SELECT TOP (1000) * FROM [dbo].[users]")
        row = cursor.fetchone()
        while row:
            print(row[0] + " " + row[1])
            row = cursor.fetchone()


