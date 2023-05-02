from flask import Flask, jsonify, request, render_template
from model import get_model

from pathlib import Path

app = Flask(__name__)
app.config["APPLICATION_ROOT"] = "/api/"


THIS_FOLDER = Path(__file__).parent.resolve()

model = get_model()

weights_file = THIS_FOLDER / "weights.h5"

model.load_weights(weights_file)

# from flask import Flask, jsonify

# app = Flask(__name__)
# app.config["APPLICATION_ROOT"] = "/api/"

@app.route('/')
def home():
    return jsonify("hello world")

@app.route('/predict', methods = ['POST'])
def predict():
    return jsonify("hello world")


if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, jsonify, request, render_template
# from model import get_model

# from pathlib import Path

# app = Flask(__name__)
# app.config["APPLICATION_ROOT"] = "/api/"


# # THIS_FOLDER = Path(__file__).parent.resolve()

# # model = get_model()

# # weights_file = THIS_FOLDER / "weights.h5"

# # model.load_weights(weights_file)


# @app.route('/')
# def home():
#     return jsonify("helloworld")
#     # return render_template("ui.html")

# @app.route('/predict', methods = ['POST'])
# def predict():
#     # input_data = [[float(i) for i in row] for row in request.json['input']]
#     # y_pred_val = model.predict(input_data)
#     # y_pred_val_labels = (y_pred_val >= 0.5).astype(int)
#     # for i in range(len(input_data)):
#     #     input_data[i].append(int(y_pred_val_labels[i][0]))
#     # return jsonify(input_data)

#     return jsonify("hi")


# if __name__ == '__main__':
#     app.run(debug=True)