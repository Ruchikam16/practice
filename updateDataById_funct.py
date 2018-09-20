import mysql.connector
import sys

def updateDataById(table_name,id,name,age,gender):
    conn=mysql.connector.connect(host='mydb.cpew7k8mfhhi.ap-south-1.rds.amazonaws.com' , user='root' , password='rootroot' , database='mydb')
    c=conn.cursor()
    sql="update "+ table_name +" set name ='"+ name +"' , age= "+ str(age) +"  , gender ='"+ gender +"' where id ="+ str(id) +" "
    c.execute(sql)
    c.execute("select * from "+ table_name +" ")
    print(c.lastrowid)
    print(c.fetchall())
    conn.commit()


table_name='employee'
id=5
name='Anil Mahajan'
age=55
gender='M'
updateDataById(table_name,id,name,age,gender)   


    
