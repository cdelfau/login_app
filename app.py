from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/") 

def authenticatedisp_loginpage():
    print "\n\n\n"
    print "***DIAG*** this Flask obj"
    print app
    #print "***DIAG*** this request obj"
    #print request
    #print "***DIAG*** request headers"
    #print request.headers
    #print "***DIAG*** request method"
    #print request.method
    #print "***DIAG*** request args['username']"
    #print request.args['username']
    #print "***DIAG*** request form"
    #print request form
    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
