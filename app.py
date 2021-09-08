from operator import concat
from flask import Flask, config,render_template,request,redirect,url_for, make_response, jsonify, session
import time
import aiml
import json
import os
import logging
import subprocess

app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/getTime", methods=['GET'])
def getTime():
    print("browser time: ", request.args.get("time"))
    print("server time : ", time.strftime('%A %B, %d %Y %H:%M:%S'));
    return "Done"

@app.route("/bot")
def bot():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
	message = str(request.form['messageText'])
	kernel = aiml.Kernel() 
	if os.path.isfile("bot_brain.brn"):
	    kernel.bootstrap(brainFile = "bot_brain.brn")
	else:
	    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
	    kernel.saveBrain("bot_brain.brn")
	# kernel now ready for use
	while True:
	    if message == "quit":
	        exit()
	    elif message == "save":
	        kernel.saveBrain("bot_brain.brn")
	    else:
	        bot_response = kernel.respond(message)
	       # print bot_response
	        return jsonify({'status':'OK','answer':bot_response})



app.run(host='localhost', debug = True, port=5000)