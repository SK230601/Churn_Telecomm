from flask import Flask,render_template,request
import config
from utils import Predict_Customer_Churn

app = Flask(__name__)

@app.route("/")
def get_home():
    return render_template("html1.html")

@app.route('/Predict', methods=['POST'])
def home():
    gender = request.form['gender']
    SeniorCitizen = int(request.form['SeniorCitizen'])
    Partner = request.form['Partner']
    Dependents = request.form['Dependents']
    PhoneService = request.form['PhoneService']
    MultipleLines = request.form['MultipleLines']
    OnlineSecurity = request.form['OnlineSecurity']
    OnlineBackup = request.form['OnlineBackup']
    DeviceProtection = request.form['DeviceProtection']
    TechSupport = request.form['TechSupport']
    StreamingTV = request.form['StreamingTV']
    StreamingMovies = request.form['StreamingMovies']
    Contract = request.form['Contract']
    PaperlessBilling = request.form['PaperlessBilling']
    MonthlyCharges = eval(request.form['MonthlyCharges'])
    TotalCharges = eval(request.form['TotalCharges'])
    tenure = int(request.form['tenure'])
    InternetService = request.form['InternetService']
    PaymentMethod = request.form['PaymentMethod']

    obj = Predict_Customer_Churn(gender,SeniorCitizen,Partner,Dependents,PhoneService,MultipleLines,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,MonthlyCharges,TotalCharges,tenure,InternetService,PaymentMethod)
    res1 = obj.get_churn()
    return render_template("Final.html",data=res1)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUM)