from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
app=Flask(__name__)
model = pickle.load(open('model.pkl', 'rb')) # read the pickle file where we develeped our ml model

@app.route('/') # creating a api
def home():
    return render_template('index.html') # this renders the template of html
@app.route('/predict',methods=['POST']) # this is my post request which is predict and i defined a fucntion predict
def predict():
    int_features = [int(x) for x in request.form.values()] # my list of values are store in x which in integers stored in object created

    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))
if __name__ == "__main__":
    app.run(debug=True)