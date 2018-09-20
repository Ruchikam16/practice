#def insertTableEmpAddr(table_name,empid,addr):
import mysql.connector

conn=mysql.connector.connect(host='mydb.cpew7k8mfhhi.ap-south-1.rds.amazonaws.com' , user='root' , password='rootroot' , database='mydb')
c=conn.cursor()
#sql_stmt = "insert into "+ table_name +"  values (('"+ empid +"' , "+ addr +" )"
sql="insert into employee_addr values(4,'hno15 street no 18 amritsar')"

c.execute(sql) 
#    c.execute("select * from " + table_name)
#    print(c.fetchall())
conn.commit()
