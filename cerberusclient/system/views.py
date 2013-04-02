from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from system.models import Message
from serializer import JSONSerializer
import simplejson

def home(request):
	return "Hello world!"

# Get the most recent notifications
def getRecentNotifs(request, n=10):
	jsonSerializer = JSONSerializer()
	notifs = Message.objects.all()
	if len(notifs) >= 10: notifs = notifs[(len(notifs) - 10):]

	return HttpResponse(jsonSerializer.serialize(notifs), 'application/json')

# Get unseen notifications
def getUnseenNotifs(request):
	jsonSerializer = JSONSerializer()
	unseenNotifs = get_list_or_404(Message, seen=False)
	return HttpResponse(jsonSerializer.serialize(unseenNotifs), 'application/json')

# Check whether there are new notifications or not
def checkForNotifs(request):
	unseenNotifs = Message.objects.filter(seen=False)
	return HttpResponse(simplejson.dumps({'count':len(unseenNotifs)}), 'application/json')

# Update notification status
def markAsSeen(request):
	notif = get_object_or_404(Message,pk=request.GET['messageID'])
	notif.seen = True
	notif.save()
	return HttpResponse(status=200)

