import plivo
from config_parser import get_config

config=get_config()
def call(number,message): 
	auth_id = config['AUTH_ID']
	auth_token =config['AUTH_TOKEN']
	p = plivo.RestAPI(auth_id, auth_token)

	params = {
    	'from': '1212121212', 
    	'to': number,
    	'answer_url' : config['BASE_URL']+'/answer?message='+message,
    	'answer_method' : "GET",
	}
	response=p.make_call(params)
	return response

def add_message(message):
	plivo_response=plivo.Response()
	plivo_response.addSpeak(message,loop=1)
	return plivo_response.to_xml()
