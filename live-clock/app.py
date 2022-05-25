#!python3 Flask 
# streaming clock per http://flask.pocoo.org/docs/1.0/patterns/streaming

from flask import Flask, Response, render_template, url_for, request
from datetime import datetime, timedelta
import time
from json import loads

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/time_feed', methods=['POST'])
def time_feed():
	
	# Get time from device
	json_data = request.data
	json_data = json_data.decode("UTF-8")
	json_data = loads(json_data)
	

	# 1. Return the right time
	# 2. Calculate offset from the time that the device has sent to us
	def get_device_time(time_data):
		return datetime.fromtimestamp((time_data["time"] // 1000))

	cur_time = datetime.now().strftime("%Y.%m.%d | %H:%M")

	return Response(f"Current time: " + cur_time + "<br>Offset: " + str(datetime.now() - get_device_time(json_data)) , mimetype='text') 

if __name__ == '__main__':
	app.run(debug=True, port=80, threaded=True, host='0.0.0.0')
