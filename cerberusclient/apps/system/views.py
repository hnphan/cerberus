from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from system.models import Message, LocalPackage
from libs.serializer import JSONSerializer
import simplejson
import shutil
from system import commands
import subprocess


def home(request):
	return "Hello world!"

def restart(request):
	subprocess.call(["shutdown /r", "-f", "-s", "-t", "60"])
	return HttpResponse(status=200)

def shutdown(request):
    subprocess.call(["shutdown", "-f", "-s", "-t", "0"])
    return HttpResponse(status=200)

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

# Package manager
def pacMan(request):
	# get all installed package
	installed_packages = LocalPackage.objects.filter(status=2)
	return render(request,'system/pacman/index.html', {'packages':installed_packages, 'title': "package manager"})

def pacManRemove(request, package_id):
	try:
		package = LocalPackage.objects.get(pk=package_id)
		# go to package local path
		path = package.location
		shutil.rmtree(path)
		title = package.title
		package.delete()
		commands.sendSystemMessage(content = "Cerberus has successfully removed " + title)
	except:
		commands.sendSystemMessage(content = "An error occurred while removing " + title)
		return HttpResponse(simplejson.dumps({'status':500}), 'application/json')
	return HttpResponse(simplejson.dumps({'status':200}), 'application/json')


