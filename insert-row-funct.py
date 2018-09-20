
import mysql.connector
import sys

def insert_table(table_name,val1,val2):

        conn=mysql.connector.connect(host='mydb.cpew7k8mfhhi.ap-south-1.rds.amazonaws.com' , user='root' , password='rootroot' , database='mydb')
        c=conn.cursor()
        
#        "insert into example values("ruchika" , 234)"
        
        sql_stmt = "insert into "+ table_name +" values('"+ val1 +"' , "+ str(val2) +")" 
        c.execute(sql_stmt)
        c.execute("select * from " + table_name)      
        print(c.fetchall())
        conn.commit()
        
    
table='example1'
val1='ankita'
val2=132

insert_table(table,val1,val2)


