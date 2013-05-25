import model

def create_group(message,numbers):
	group=model.group()
	group.message=message
	group.numbers=numbers
	group.save()
	print "Created Group"
def update_group(message,numbers,group_id):
	group=model.group.objects.get(id=group_id)
	group.message=message
	group.numbers=numbers
	group.save()
	print "Group %s updated",group_id


