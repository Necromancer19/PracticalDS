import mysql.connector as mysql

conn = mysql.connect(host='localhost',
                     database='DataScience',
                     user='root',
                     password='root')

conn.connect
if(conn.is_connected):
    print('Connection With MySql Established Successfullly')
else:
    print('Not Connected -- Check Connection Properites')

