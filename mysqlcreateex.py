#py -m pip install oracle
#py -m pip uninstall mysql-connector
#(latest version)
#py -m pip install  mysql-connector-python       
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="socgen")

mycursor=mydb.cursor()

mycursor.execute("create table emps(empid  int,ename varchar(10))");
print("Table Created")