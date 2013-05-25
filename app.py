from flask import Flask,request,Response,render_template,redirect,url_for,make_response
import json
import plivo_helper
from models import group
from redis import Redis
from rq import Queue
app=Flask(__name__)
app.debug=True

job_queue=Queue(connection=Redis())

@app.route('/')
def index():
	return render_template('index.html') 


@app.route('/call',methods=['POST'])
def call():

	message=request.form['message']
	numbers=[int(request.form['number'+str(i)])for i in range(1,6)]
	group.create_group(message,numbers)
	for number in numbers:
		job_queue.enqueue(plivo_helper.call,number,message)
	return "Successfully submitted to the queue"

		

@app.route('/answer')
def answer():
	message=request.args.get('message')
	response=make_response(plivo_helper.add_message(message))
	response.headers['Content-Type']='text/xml'
	return response

if __name__=='__main__':
	app.run()
