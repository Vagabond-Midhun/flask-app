import mysql.connector
def get_data():
    mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="testdb")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM employee")
    result = mycursor.fetchmany()

    mydb.close()
    return result