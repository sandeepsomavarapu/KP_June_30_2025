
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="socgen")

mycursor=mydb.cursor()

mycursor.execute("update emps set ename='sandeep' where empid=127");

mydb.commit();