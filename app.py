'''Chloe Delfau
SoftDev1 pd 8
HW 04 -- Into a Zone of Danger
2016-09-29'''  

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")

def home():
    print '\n\n***DIAG***this Flask obj'
    print app

    print "\n\n***DIAG***this request obj"
    print request

    print "\n***DIAG***request.headers"
    print request.headers

    print "\n***DIAG***request.method"
    print request.method

    print "\n***DIAG***request.args"
    print request.args

    print "\n***DIAG***request.form"
    print request.form

    return render_template("login.html", title="Home")
    
@app.route("/auth", methods = ['POST']) 

def authenticate():
#    print "\n\n***DIAG***this Flask obj"
#    print app
    
#    print "\n***DIAG***this request obj"
#    print request

#    print "\n***DIAG***request.headers"
#    print request.headers

#    print "\n***DIAG***request.method"
#    print request.method

#    print "\n***DIAG***request.args"
#    print request.args

#    print "\n***DIAG***request.form['username']"
#    print #request.form['username']
    
    if request.form['username'] == "Asterix" and request.form['password'] == "password":
        return render_template("auth.html", status = "Success")
    return render_template("auth.html", status = "Failure")

if __name__ == "__main__":
    app.debug = True
    app.run()
