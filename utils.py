import config
import json
import pickle
import numpy as np

class Predict_Customer_Churn():
    def __init__(self,gender,SeniorCitizen,Partner,Dependents,PhoneService,MultipleLines,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,MonthlyCharges,TotalCharges,tenure,InternetService,PaymentMethod):
        self.gender             = gender
        self.SeniorCitizen      = SeniorCitizen
        self.Partner            = Partner
        self.Dependents         = Dependents
        self.PhoneService       = PhoneService
        self.MultipleLines      = MultipleLines
        self.OnlineSecurity     = OnlineSecurity
        self.OnlineBackup       = OnlineBackup
        self.DeviceProtection   = DeviceProtection
        self.TechSupport        = TechSupport
        self.StreamingTV        = StreamingTV
        self.StreamingMovies    = StreamingMovies
        self.Contract           = Contract
        self.PaperlessBilling   = PaperlessBilling
        self.MonthlyCharges     = MonthlyCharges
        self.TotalCharges       = TotalCharges
        self.tenure             = tenure
        self.InternetService    = InternetService
        self.PaymentMethod      = PaymentMethod

    def load_model(self):
        with open(config.MODEL_PATH_DT,"rb") as f:
            self.model = pickle.load(f)
        with open(config.JSON_PATH,"r") as f1:
            self.json_data = json.load(f1)

    def encoding(self):
        if self.tenure > 0 and self.tenure <= 12:
            Tenure1 = 1
        elif self.tenure > 12 and self.tenure <= 24:
            Tenure1 = 2
        elif self.tenure > 24 and self.tenure <= 36:
            Tenure1 = 3
        elif self.tenure > 36 and self.tenure <= 48:
            Tenure1 = 4
        elif self.tenure > 48 and self.tenure <= 60:
            Tenure1 = 5
        else:
            Tenure1 = 6
        return Tenure1

    def get_churn(self):
        self.load_model()
        array = np.zeros(len(self.json_data["columns"]),dtype=float)
        array[0]  = self.json_data["gender_val"][self.gender]
        array[1]  = self.SeniorCitizen
        array[2]  = self.json_data["partner_val"][self.Partner]
        array[3]  = self.json_data["dependents_val"][self.Dependents]
        array[4]  = self.json_data["phone_service_val"][self.PhoneService]
        array[5]  = self.json_data["multiple_lines_val"][self.MultipleLines]
        array[6]  = self.json_data["online_security_val"][self.OnlineSecurity]
        array[7]  = self.json_data["online_backup_val"][self.OnlineBackup]
        array[8]  = self.json_data["device_protection_val"][self.DeviceProtection]
        array[9]  = self.json_data["tech_support_val"][self.TechSupport]
        array[10] = self.json_data["streaming_tv_val"][self.StreamingTV]
        array[11] = self.json_data["streaming_movies_val"][self.StreamingMovies]
        array[12] = self.json_data["contract_val"][self.Contract]
        array[13] = self.json_data["paper_less_billing_val"][self.PaperlessBilling]
        array[14] = self.MonthlyCharges
        array[15] = self.TotalCharges
        array[16] = self.encoding()

        InternetService_1 = "InternetService_" + self.InternetService
        InternetService_index = self.json_data["columns"].index(InternetService_1)
        array[InternetService_index] = 1

        PaymentMethod_1 = "PaymentMethod_" + self.PaymentMethod
        PaymentMethod_index = self.json_data["columns"].index(PaymentMethod_1)
        array[PaymentMethod_index] = 1

        print("Input Array for Model = ",array)
        pred_churn = self.model.predict([array])[0]
        return pred_churn
    
if __name__ == "__main__":
    gender            = "Male"
    SeniorCitizen     = 0
    Partner           = "No"
    Dependents        = "No"
    tenure            = 2
    PhoneService      = "Yes"
    MultipleLines     = "No"
    InternetService   = "DSL"      
    OnlineSecurity    = "Yes"
    OnlineBackup      = "Yes"
    DeviceProtection  = "No"
    TechSupport       = "No"
    StreamingTV       = "No"
    StreamingMovies   = "No"
    Contract          = "Month-to-month"
    PaperlessBilling  = "Yes"
    PaymentMethod     = "Mailed check"
    MonthlyCharges    = 53.85
    TotalCharges      = 108.15
    obj = Predict_Customer_Churn(gender,SeniorCitizen,Partner,Dependents,PhoneService,MultipleLines,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,MonthlyCharges,TotalCharges,tenure,InternetService,PaymentMethod)
    res = obj.get_churn()
    print("Predicted Customer Churn - ",res)