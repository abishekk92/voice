from mongoengine import *


connect('voice')

class group(Document):
	message=StringField()
	numbers=ListField(IntField())
