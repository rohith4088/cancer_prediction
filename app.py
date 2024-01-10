from flask import Flask,render_template,jsonify,app,request,url_for
import numpy as np
import pandas as pd
import pickle
app = Flask(__name__)
#load the model
model = pickle.load(open("knn_model.pkl",'rb'))
scaler = pickle.load(open("scaling.pkl",'rb'))
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict_api',methods = ['POST']) 
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(new_data)
    print(output)
    return jsonify(output.tolist())
@app.route('/predict',methods = ['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output = model.predict(final_input)
    return render_template("home.html",prediction_text = "The Predicted Result Is -->{}".format(output))
    
if __name__ == "__main__":
    app.run(debug = True)
    