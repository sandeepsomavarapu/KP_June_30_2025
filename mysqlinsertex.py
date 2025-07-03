
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="socgen")

mycursor=mydb.cursor()

mycursor.execute("insert into emps values(127,'rajesh')");

mydb.commit();