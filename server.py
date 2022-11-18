import pandas as pd
from flask import Flask, request, jsonify
from waitress import serve
import pickle
# install flask, waitress, pickle into your ananconda environment

app = Flask(__name__)
modelOne = pickle.load(open('model1.pkl', 'rb')) # load model1 to the server, 'rb' - read binary
df_time_series = pd.read_pickle('model2.pkl')
df_time_series1 = pd.read_pickle('model21.pkl')

@app.route('/model1', methods=['GET','POST'])
def callModelOne():
    data = request.get_json(silent=True)
    if data is None:
        x1Value = request.headers.get('x1',type=float) or request.args.get('x1', type=float) or request.form.get('x1', type=float)
        x2Value = request.headers.get('x2',type=float) or request.args.get('x2', type=float) or request.form.get('x2', type=float)
        y1Value = request.headers.get('y1',type=float) or request.args.get('y1', type=float) or request.form.get('y1', type=float)
        y2Value = request.headers.get('y2',type=float) or request.args.get('y2', type=float) or request.form.get('y2', type=float)
    else:
        x1Value = data.get('x1',type = float)
        x2Value = data.get('x2',type = float)
        y1Value = data.get('y1',type = float)
        y2Value = data.get('y2',type = float)

    if x1Value is None or x2Value is None or y1Value is None or y2Value is None:
        return jsonify({"message" : "Invalid input"})
    if x1Value < 0 or x2Value < 0 or y1Value < 0 or y2Value < 0:
        return jsonify({"message" : "Input only positive values"})
    else:
        return jsonify({"result" : str(modelOne.predict([[x1Value,x2Value,y1Value,y2Value]]))[2:-2]})
        
@app.route('/model2', methods=['GET','POST'])
def callModelTwo():
    xValue = request.get_json(silent=True) or request.headers.get('x', type=int) or request.args.get('x', type=int) or request.form.get('x', type=int)
    if isinstance(xValue,int):
        if xValue>250 or xValue < 50:
            return jsonify({"message":'Invalid input! Please enter a number between 50 to 250'})
        else:
            return jsonify({"result": str(df_time_series[xValue])})
    else:
        return jsonify({"message" : "Invalid input! Please enter an integer"})
# run the server
if __name__ == '__main__':
    print("Starting the server.....")
    serve(app, host="0.0.0.0", port=5000)