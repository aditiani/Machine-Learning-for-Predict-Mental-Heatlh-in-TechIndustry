from flask import Flask, jsonify, render_template, request
import json
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/', methods= ['POST','GET'])
def home() :
   return render_template('index.html')

@app.route('/profile', methods= ['POST','GET'])
def profile() :
   return render_template('profile.html')

@app.route('/result', methods= ['POST','GET'])
def result():
    if request.method == 'POST':
        input= request.form

        mh_predict = pd.DataFrame({
            'Gender': [input['Gender']],
            'Self_Employed': [input['Self_Employed']],
            'Family_History': [input['Family_History']],
            'Work_Interfere': [input['Work_Interfere']],
            'Employee_Numbers': [input['Employee_Numbers']],
            'Tech_Company': [input['Tech_Company']],
            'Benefits': [input['Benefits']],
            'Care_Options': [input['Care_Options']],
            'Seek_Help': [input['Seek_Help']],
            'Anonymity': [input['Anonymity']],
            'Medical_Leave': [input['Medical_Leave']],
            'Mental_Health_Consequence': [input['Mental_Health_Consequence']],
            'Coworkers': [input['Coworkers']],
            'Supervisor': [input['Supervisor']],
            'Mental_Health_Interview': [input['Mental_Health_Interview']],
            'Physical_Health_Interview': [input['Physical_Health_Interview']],
            'Mental_VS_Physical': [input['Mental_VS_Physical']],
            'Observed_Consequence': [input['Observed_Consequence'],]
        })

        prediksi= model.predict_proba(mh_predict)[0][1]

        if prediksi>0.5:
            pred= 'Get Treatment'
        else:
            pred= 'No Treatment'

        return render_template('result.html', data= input, pred= pred, prob= round(prediksi, 2))

if __name__ == '__main__':
    filename= 'Final_Project.sav'
    model= pickle.load(open(filename, 'rb'))
    app.run(debug=True)
