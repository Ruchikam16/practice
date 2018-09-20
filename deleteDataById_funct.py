import mysql.connector
import sys

def deleteDataById(table_name,emp_id):
    conn=mysql.connector.connect(host='mydb.cpew7k8mfhhi.ap-south-1.rds.amazonaws.com' , user='root' , password='rootroot' , database='mydb')
    c=conn.cursor()
    sql="delete from  "+ table_name +" where emp_id ="+ str(id) +" "
    c.execute(sql)
    c.execute("select * from "+ table_name +" ")
#   print(c.lastrowid)
    print(c.fetchall())
    conn.commit()


table_name='employee_addr'
id=2
deleteDataById(table_name,id)


    
