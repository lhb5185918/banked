from flask import Flask,request,jsonify
from bankedutil.weather import wea
from bankedutil.cos import getCos

app = Flask(__name__)


@app.route('/weather',methods = ['GET'])
def get_weather():
    res = wea()
    return res

@app.route('/weatherPicture',methods = ['GET'])
def get_weatherPicture():
    res = getCos().getWeatherPicture()
    return res


if __name__ == '__main__':
    app.run(host="0.0.0.0",port =80)
