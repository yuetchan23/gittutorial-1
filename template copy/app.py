from flask import Flask, render_template  #NEW IMPORT!!

app = Flask(__name__)    #This is creating a new Flask object

#decorator that links...

@app.route('/')          						#This is the main URL
def default():
    return render_template("index.html", name="index",title = "Home Page")		#The argument should be in templates folder

@app.route('/index')          						#This is the main URL
def index():
    return render_template("index.html", name="index",title = "Home Page")

@app.route('/interests')
def interests():
    return render_template("interests.html", name ="interests",title = "Interests Page")

#@app.route('/interests')
@app.route('/courses')
def courses():
    return render_template("courses.html", name ="courses",title = "Courses Page")

#Add the code for other
@app.route('/other')
def other():
    return render_template("other.html", name ="other",title = "Other Page")
#Hmmm, do we need another one?


if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional
