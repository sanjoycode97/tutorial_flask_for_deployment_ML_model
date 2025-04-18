from flask import Flask,render_template,request
import joblib


#initialize app

app=Flask(__name__)

model = joblib.load('../saving_model/saved_logitic_model.pkl')

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

@app.route("/pred")
def predictions():
    return render_template("data_input.html")

@app.route("/action",methods=["POST"])
def action():
    #return "form has been submitted successfully"
    data=[]
    for val in request.form.values():
        data.append(val)
    print(data)

    return f'data successfully added'

@app.route("/ML_pred")
def ML_predictions():
    return render_template("ML_form.html")

@app.route("/pred_result",methods=["POST"])
def pred_result():
    #return "form has been submitted successfully"
    data=[]
    for val in request.form.values():
        data.append(float(val))
    result=model.predict([data])

    print(result)

    if result[0]==1:
        return 'pateint is diabetic'
    return f'pateient not diabetic'




#run the app
app.run(debug=True)