#SOLVED 
#HOW TO CONNECT TO MS SQL SERVER VIA PYTHON OM MAC OS (using pyodbc)

import pyodbc

server = '000.000.0.0' # IP
port = '1433' # defualt port for MS SQL Server
db = 'DATABASE' 
user='USER' 
password='PASSWORD' 

cn = pyodbc.connect('DRIVER=/usr/local/lib/libtdsodbc.so;SERVER={server};PORT={port};DATABASE={db};UID={user};PWD={password}'.format(server=server,port=port,db=db, user=user,password=password))

cursor = cn.cursor()

sql = 'SELECT * FROM SOMETABLE' #sql string

cursor.execute(sql)

for i in cursor.fetchall():
    print(i)
