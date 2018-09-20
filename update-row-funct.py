
import mysql.connector
import sys

def update_table(table_name,cols1,cols2,val1,val2):
#       with conn:

        conn=mysql.connector.connect(host='mydb.cpew7k8mfhhi.ap-south-1.rds.amazonaws.com' , user='root' , password='rootroot' , database='mydb')
        c=conn.cursor()
                 
        sql_stmt = "update "+ table_name +"  set "+ cols1 +" ='"+ val1 +"' , "+ cols2 +" = "+ str(val2) +""
        #where "+ cols2 +" = "+ str(val2) +""
        c.execute(sql_stmt) 
        c.execute("select * from " + table_name)
        print(c.fetchall())
        conn.commit()
    
table='example1'
cols1='name'
cols2='rollid'
val1='ankita'
val2=123

update_table(table,cols1,cols2,val1,val2)


