import sqlite3
import json
conn=sqlite3.connect("python.db")

data={}
data['name']="Ruchika"
data['age']=23
addr={}
addr['city']="Amritsar"
addr['stat']="Punjab"
data['loc']=addr
data1={}
data1['name']="Prateek"
data1['age']=23
"""rows=[]
rows.append[data]
rows.append[data1]
for row in rows:"""
print(json.dumps(data))
print(json.dumps(data1))


