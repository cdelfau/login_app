'''Chloe Delfau
SoftDev1 pd 8
HW 04 -- Into a Zone of Danger
2016-10-04''' 

#all of the necessary imports
from flask import Flask, render_template, request
import hashlib
import csv

#create the flask app
app = Flask(__name__)
data = dict()

#home route
@app.route("/")
def home():
    readFile()
    return render_template("login.html")

#the route when you register for 
@app.route("/register", methods=['POST'])
def register():
    usr = request.form["usr"] #register with a username
    pw = request.form["pw"] #register with a password
    if usr == "" or pw == "": #if either the username or the password is invalid
        return "<center>Please fill in both the username and password textboxes!</center>"
    elif usr in data: #username already exists
        return "<center>Username already exist please try a new one!</center>"
    else: #the username is unique and botht eh username and password are valid
        hashObj = hashlib.sha1()
        hashObj.update(pw) #hashcode the password
        postPw = hashObj.hexdigest()
        writeFile(usr,postPw) #add the username and hashed password to the csv file
        readFile()
        return render_template("register_success.html")

#route for new register page html
@app.route("/registerNew", methods=['POST'])
def registerPage():
    return render_template("register.html")

#route to check login
@app.route("/auth", methods=['POST'])
def loginCheck():
    hashObj = hashlib.sha1()
    usr = request.form["usr"] #get the username
    hashObj.update(request.form["pw"]) #hash the password submitted
    pw = hashObj.hexdigest() #compare hashed password submitted and existing password for the username
    if usr in data:
        if data[usr] == pw:
            return "<center>Login Success!</center>" #correct password!
        else:
            return "<center>Incorrect password!</center>" #incorrect password
    else:
        return "<center>User name doesn't exist!</center>" #user doesnt exist, make a new user

#read into the csv file
def readFile():
    with open('data.csv','r') as csvfile:
        dataReader = csv.reader(csvfile)
        for row in dataReader:
            if row[0] != "Usr" and row[1] != "Pw" and (row[0] not in data) :
                data[row[0]] = row[1]

#write into the csv file
def writeFile(u,p):
    with open('data.csv','w') as csvfile:
        dataWriter = csv.writer(csvfile)
        dataWriter.writerow([u,p])

#debug
if __name__ == "__main__":
    app.debug = True
    app.run() 
