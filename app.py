from flask import Flask,request,Response,render_template
import plivo
import json
app=Flask(__name__)
BASE_URL="127.0.0.1:5000"

def make_call(number,message): 
	auth_id = ""
	auth_token = ""

	p = plivo.RestAPI(auth_id, auth_token)

	params = {
    	'from': '1212121212', 
    	'to': number,
    	'answer_url' : BASE_URL+"/answer?"+message,
    	'answer_method' : "GET",
	}
	response=p.make_call(params)
	print response
	return response

@app.route('/')
def index():
	return render_template('index.html') 


@app.route('/call')
def call():
	number=request.args.get('number')
	message=request.args.get('message')
	print message
	response=make_call(number,message)
	return Response(json.dumps(response),mimetype='application/json')
@app.route('/answer')
def answer():
	message=request.args.get('message')
	plivo_response=plivo.Response()
	plivo_response.addSpeak(message,loop=1)
	return render_template('response.xml',response=plivo_response)
if __name__=='__main__':
	app.run()
