import mysql.connector
conn=mysql.connector.connect(host='mydb.cpew7k8mfhhi.ap-south-1.rds.amazonaws.com' , user='root', password='rootroot' , database='mydb')
c=conn.cursor()
data=[('prateek',133),
      ('anil',135),
      ('renu',136),
      ('ankita',322)]
#c.execute("insert into student values('ankita',122)")
sql="insert into student values(%s,%s)"
c.executemany(sql,data)
c.execute("select * from student")
print(c.fetchall())
conn.commit()

