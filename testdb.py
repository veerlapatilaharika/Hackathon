import mysql.connector
conn=mysql.connector.connect(
    host='127.0.0.1',
    database='stockordersystem',
    user='root',
    password='rootqwer',
    auth_plugin='mysql_native_password')
# conn=pyodbc.connect(conn_str)
cursor=conn.cursor()
cursor.execute("SELECT * FROM ordertype;")
for row in cursor:
    print(row)