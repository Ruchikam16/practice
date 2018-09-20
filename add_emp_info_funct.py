
import mysql.connector
import sys

"""def createTableEmpAddr(table_name,cols1,cols2):

        conn=mysql.connector.connect(host='mydb.cpew7k8mfhhi.ap-south-1.rds.amazonaws.com' , user='root' , password='rootroot' , database='mydb')
        c=conn.cursor()

        c.execute("drop table if exists " + table_name);
        sql_stmt = "create table "+ table_name +"  ("+ cols1 +" int(4),"+ cols2 +" varchar(255))" 
        c.execute(sql_stmt) 
        c.execute("select * from " + table_name)
        print(c.fetchall())

table='employee_addr'
cols1='emp_id'
cols2='addr_line'
createTableEmpAddr(table ,cols1,cols2) """



def insertTableEmpAddr(table_name,empid,addr):
        
    conn=mysql.connector.connect(host='mydb.cpew7k8mfhhi.ap-south-1.rds.amazonaws.com' , user='root' , password='rootroot' , database='mydb')
    c=conn.cursor()

    sql_stmt = "insert into "+ table_name +"  values ("+ str(empid) +" , '"+ addr +"' )"
    c.execute(sql_stmt) 
    c.execute("select * from " + table_name)
    print(c.fetchall())
    conn.commit()

table='employee_addr'
empid=3
addr='hno15 merut'


insertTableEmpAddr(table,empid,addr)
