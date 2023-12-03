from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data and convert to float
    input_data = {
        "bedrooms": float(request.form['bedrooms']),
        "bathrooms": float(request.form['bathrooms']),
        "sqft_living": float(request.form['sqft_living']),
        "sqft_lot": float(request.form['sqft_lot']),
        "floors": float(request.form['floors']),
        "waterfront": float(request.form['waterfront']),
        "view": float(request.form['view']),
        "condition": float(request.form['condition']),
        "grade": float(request.form['grade']),
        "sqft_above": float(request.form['sqft_above']),
        "sqft_basement": float(request.form['sqft_basement']),
        "yr_built": float(request.form['yr_built']),
        "yr_renovated": float(request.form['yr_renovated']),
        "zipcode": float(request.form['zipcode']),
        "lat": float(request.form['lat']),
        "long": float(request.form['long']),
        "sqft_living15": float(request.form['sqft_living15']),
        "sqft_lot15": float(request.form['sqft_lot15']),
    }

    # Make a request to the FastAPI endpoint
    response = requests.post("http://service1:8000/predict", json=input_data)
    prediction = response.json()["prediction"]

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
