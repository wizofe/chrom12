import pymysql
import json
# parameters
dbname = 'chrom12'
dbhost = 'localhost'
dbuser = 'root'
dbpass = ''
port = 3306

db =pymysql.connect(dbhost, dbuser,dbpass,dbname)
cursor=db.cursor()
sql='SELECT * FROM test'
cursor.execute(sql)
test = list(cursor.fetchall())
test1 = json.dumps(test)
print(test)
print(test1)
