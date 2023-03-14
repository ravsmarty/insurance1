from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)

file=open("model_final.pkl","rb")
model=pickle.load(file)

    
@app.route('/')
def home():
    return render_template('index2.html')

@app.route("/account_data", methods=["POST"])
def get_data():
    Age = request.form["Age"]
    Gender = request.form["Gender"]
    BMI = request.form["BMI"]
    childrens = request.form["no_of_children"]
    smoker = request.form["Smoker_or_not"]
    Region = request.form["Enter_your_Region"]
    Charges = request.form["Charges"]
    
    output=model.predict(np.array([[Age,Gender,BMI,childrens,smoker,Region,Charges]]).reshape(1,-1))

    if output[0]==1:
      return "claim"
    else:
      return "no claim"

app.run(port=8080)