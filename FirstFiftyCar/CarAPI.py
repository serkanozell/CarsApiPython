from flask import Flask, jsonify
from flask import make_response
from flask import request



app = Flask(__name__)

@app.route('/azon/api/cars/list',methods=['GET'])
def get_cars():
    return jsonify({'cars':cars})

@app.route('/azon/api/cars/<string:extcolor>',methods=['GET'])
def get_car_by_brand(car_color):
    car = [car for car in cars if car['color'] == extcolor]
    return jsonify({'car':car})

@app.route('/azon/api/cars/<string:car_transmission>',methods=['GET'])
def get_car_by_transmission(car_transmission):
    transmission = [car for car in cars if car['transmission'] == car_transmission]
    return jsonify({'car':car})

