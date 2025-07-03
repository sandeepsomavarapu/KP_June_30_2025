
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="ericsson_hyd")

mycursor=mydb.cursor()

mycursor.execute("select * from emps")
data =mycursor.fetchall()
 
for row in data:
        print("Employee Number:",row[0])
        print("Employee Name:",row[1])
        print("Employee Salary:",row[2])
        print("Employee Designation:",row[3])

eid=111
mycursor.execute(f"SELECT * FROM emps where eid={eid}")

myresult = mycursor.fetchone()

print(myresult)
#for x in myresult:
#  print(x)