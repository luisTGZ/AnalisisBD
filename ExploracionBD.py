import mysql.connector
import time


dbconect = {
    "host":"localhost",
    "user":"root",
    "password":"luis",
    "database":"moodle",
    "port":"3306"
}
j = 0
myresult2 = ""

while True:
    time.sleep(.2)
    conexion= mysql.connector.connect(**dbconect)
    mycursor = conexion.cursor()
    sql="SELECT id,userid,courseid,component,action,target,objecttable,other FROM mdl_logstore_standard_log ORDER BY id DESC limit 1;"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if myresult != myresult2:
        myresult2 = myresult;
        for row in myresult:
            j += 1
            print(j)
            print("id, useris,courseid, component, action, target, objecttable, other" )
            print(row)

    conexion.close()