from flask import Flask, jsonify

app = Flask(__name__)
app.config["APPLICATION_ROOT"] = "/api/"

@app.route('/')
def home():
    return jsonify("hello world")

@app.route('/predict', methods = ['POST'])
def predict():
    return jsonify("hello world")


if __name__ == '__main__':
    app.run(debug=True)