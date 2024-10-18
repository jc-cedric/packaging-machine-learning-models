from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

#load the model
model = joblib.load('./models/rf_model.pkl')

#define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
  #get the data from the POST request
  data = request.get_json()
  #reshape input
  input_data = np.array(data['input']).reshape(1,-1)
  prediction = model.predict(input_data)
  
  return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
  app.run(debug=True)  #run the app in debug mode