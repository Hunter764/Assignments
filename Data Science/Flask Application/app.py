from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

#####

db_config = {
    'host': 'localhost',
    'database': 'registration_db',
    'user': 'root',
    'password': 'Durgesh@18'
}

@app.route("/")
def registration_form():
    return render_template('registration.html')

try:
    db_connection = mysql.connector.connect(**db_config)
    if db_connection.is_connected():
        print("Success")
except Error as e:
    print(e)

@app.route('/register', methods= ['GET', 'POST'])
def register():
    if request.method == 'post':
        StudentName = request.form['StudentName']
        FatherName = request.form['FatherName']
        MotherName = request.form['MotherName']
        PhoneNumber = request.form['MobileNumber']
        Email = request.form['Email']
        DOB = request.form['DOB']
        Address = request.form['Address']
        BloodGroup = request.form['BloodGroup']
        Department = request.form['Department']
        Course = request.form['Course']
        Password = request.form['Password']


        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (Student_Name, Father_Name, Mother_Name, Phone_Number, Email, DOB, Address, Blood_Group, Department, Course, Password) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)", (StudentName, FatherName, MotherName, PhoneNumber, Email, DOB, Address, BloodGroup, Department, Course, Password))
        #cursor.execute(EXECUTEquery,(StudentName, FatherName, MotherName, PhoneNumber, Email, DOB, Address, BloodGroup, Department, Course, Password))
        db_connection.commit()
        cursor.close()

        return "Registration Successful!"
    else:
        return render_template('register.html')










