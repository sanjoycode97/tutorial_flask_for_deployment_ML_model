from flask import Flask,render_template


#initialize app

app=Flask(__name__)

#create the route using the decorator
@app.route("/")
def welcome_func():
    return render_template("welcome.html")

@app.route("/review")
def review():
    return render_template("review.html")

@app.route("/contact-us")
def contact():
    return render_template("contact.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")


#run the app
app.run(debug=True)