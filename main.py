# from flask import Flask, jsonify
# from threading import Thread
# import pandas as pd

# event_data = pd.read_csv('events.txt')
# print(event_data.to_string())
# app = Flask('')
# @app.route('/')	
# def home():
# 	return  "I'm alive"

# @app.route('/api/add/num=<int:num1>&numt=<int:num2>', methods=['GET'])
# def add(num1,num2):
#   return jsonify({f"{num1}+{num2}":num1+num2})

# @app.route('/post', methods=["POST"])
# def testpost():
#      input_json = request.get_json(force=True) 
#      # dictToReturn = {'text':input_json['text']}
#      return jsonify(input_json)

# def run():
# 	app.run(host='0.0.0.0',port=7000)

# t = Thread(target=run)
# t.start()

from flask import Flask, request, jsonify
from threading import Thread
import pandas as pd

app = Flask(__name__)
event_data = pd.read_csv('events.csv')
user_data = pd.read_csv('users.csv')

@app.route('/', methods=["POST","GET"])
def hello_world():
  return jsonify({"message":"Please change api url to actually get results"})

@app.route('/post', methods=["POST"])
def testpost():
  input_json = request.get_json(force=True) 
  dictToReturn = {'text':input_json['text']}
  return jsonify(dictToReturn)

@app.route('/createUser', methods=["POST"])
def createUser():
  user_json = request.get_json(force=True)
  # id= max(axis=0)
  try:
    username = user_json['username']
    password = user_json['password']
    computer_os = user_json['computer_os']
    add_info = add_info['add_info']
  return jsonify({"max_id":6})

def run():
	app.run(host='0.0.0.0',port=7000)

t = Thread(target=run)
t.start()