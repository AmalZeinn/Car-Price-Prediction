from flask import Flask, render_template, request
import joblib
import numpy as np
import sklearn 


app = Flask(__name__)

model = joblib.load('Car_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

   try:
       
    kms_input = float(request.form.get('Driven_kms'))
    kms_log = np.log1p(kms_input)

    transmission = request.form.get('Transmission')
    fuel_type = request.form.get('Fuel_Type')
    seller_type = request.form.get('Seller_Type')

    trans_manual = 1 if transmission == 'Manual' else 0

    seller_individual = 1 if seller_type == 'Individual' else 0

    fuel_diesel = 0
    fuel_petrol = 0

    if fuel_type == 'Diesel':
       fuel_diesel = 1
    elif fuel_type == 'Petrol':
      fuel_petrol = 1

    age =float(request.form.get('age'))
    present_price = float(request.form.get('Present_Price'))

    if present_price <= 0 or kms_input < 0 or age < 0:
        return render_template('index.html', prediction_text="Error: Please enter valid positive numbers!")

    features = [
        present_price,
        kms_log,
        float(request.form.get('Owner')),
        age,
        fuel_diesel ,
        fuel_petrol ,
        seller_individual,
        trans_manual  
    ]
    
    final_features = np.array([features])
    
    
    scaled_data = scaler.transform(final_features)
    
    
    prediction = model.predict(scaled_data)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f'Estimated Car Price: ${output} ',result=request.form)
   except ValueError: 
       return render_template('index.html', prediction_text=f'Estimated Car Price: ${output}',result=request.form)

if __name__ == '__main__':
    app.run(debug=True)