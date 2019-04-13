#SOLVED 
#HOW TO CONNECT TO MS SQL SERVER VIA PYTHON OM MAC OS (using pymssql)

import pymssql

cn = pymssql.connect(host="000.000.0.0", # IP
                    user="USER",
                    password="PASSWORD",
                    database="DATABASE")


cursor = cn.cursor()

sql = 'SELECT * FROM SOMETABLE'

cursor.execute(sql)

for i in cursor.fetchall():
    print(i)
