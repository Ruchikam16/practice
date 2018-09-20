import sqlite3
import json
conn=sqlite3.connect("python.db")
c=conn.cursor()
#c.execute("drop table example")
c.execute("create table example('name' , age , rollno)")
c.execute("insert into example values('prateek13',18,162)")
c.execute("select name , age , rollno from abc")
out_data=c.fetchall()
for row in out_data:
    print(row[name])
#json_output=json.dumps(c.fetchall())
#print(json_output)  
