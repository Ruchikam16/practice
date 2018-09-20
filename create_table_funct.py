
import mysql.connector
import sys
#conn=mysql.connector.connect(host='mydb.cpew7k8mfhhi.ap-south-1.rds.amazonaws.com' , user='root' , password='rootroot' , database='mydb')
def create_table(table_name,cols1,cols2):
#       with conn:

        conn=mysql.connector.connect(host='mydb.cpew7k8mfhhi.ap-south-1.rds.amazonaws.com' , user='root' , password='rootroot' , database='mydb')
        c=conn.cursor()

        c.execute("drop table if exists " + table_name);
        sql_stmt = "create table "+ table_name +"  ("+ cols1 +" varchar(255),"+ cols2 +" int(4))" 
        c.execute(sql_stmt) 
        c.execute("select * from " + table_name)
        print(c.fetchall())
    
table='example1'
cols='name'
cols2='rollid'
#conn="mysql.connector.connect(host='mydb.cpew7k8mfhhi.ap-south-1.rds.amazonaws.com' , user='root' , password='rootroot' , database='mydb')"

create_table(table,cols,cols2)


