import RPi.GPIO as GPIO
import sys
import time
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS


led_list=[2,3,4,17,27,22,10,9,11,5]
app = Flask(__name__)
CORS(app)
api = Api(app)

GPIO.setmode(GPIO.BCM)

        
class LedConctroller(Resource):
    
    def get(self, type):
        print(type)
        if(type=="ON"):
            for pin in led_list:
                GPIO.setup(pin,GPIO.OUT)
                time.sleep(0.1)

        if(type=="OFF"):
            for pin in led_list:
                time.sleep(0.1)
                GPIO.setup(pin,GPIO.IN)
            
        return {};


api.add_resource(LedConctroller, '/led/<string:type>')

if __name__ == '__main__':
    app.run(threaded=True, port=8080, host='0.0.0.0')
