import MySQLdb as mysql
import time
import json


db = mysql.connect(host='localhost', user='root',
                   password='root', db="INFORMATION_SCHEMA")
cur = db.cursor()

cur.execute('SHOW STATUS')
res = cur.fetchall()

r = dict(res)

print(
    f"Uptime : {r['Uptime']}")
print(
    f"Thread created : {r['Threads_created']}")
print(
    f"Threads connected : {r['Threads_connected']}")
print(
    f"Threads running : {r['Threads_running']}")
print(
    f"Queries : {r['Queries']}")
print(
    f"Max_used_connections : {r['Max_used_connections']}")

cur.close()
