from flask import Flask,render_template,request
import numpy as np
import pickle
model=pickle.load(open('model.pkl','rb'))


f1=Flask(__name__)


@f1.route("/")
def home():
    return render_template("page.html")


@f1.route("/getpredict",methods=['GET','POST'])
def predict():
    features=[float(x) for x in request.form.values()]
    final_features= [np.array(features)]
    prediction=model.predict(final_features)
    output=prediction[0]
    if output ==1:
        return render_template('page.html',prediction_text='successful')
    else:
        return render_template('page.html',prediction_text='Canceled')
    
if __name__=="__main__":
    f1.run(debug=True)