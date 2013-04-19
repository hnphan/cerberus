from django.shortcuts import render
from apps.system.models import LocalPackage
from django.http import HttpResponse
import os


# Create your views here.
def home(request):
	installed_packages = LocalPackage.objects.filter(status=2)
	return render(request,'games/index.html', {'packages':installed_packages, 'title': "installed games"})

def package_action(request, package_id):
	if request.GET['command'] == "start":
		try:
			print "trying to start the game..."
			package = LocalPackage.objects.get(pk=package_id)
			# go to package local path
			path = package.location
			path_to_settings = os.path.join(path, "settings.cer")
			print "settings file in " + path_to_settings
			cd_command = "cd " + path
			# look for command text file
			with open(path_to_settings) as f:
				start_command = f.readline()
				print "found start command: " + start_command
				print "cd_command: " + cd_command
				path_to_exe = os.path.join(path, start_command)
				#os.system(cd_command)
				os.system(path_to_exe)
			# launch the command
		except:
			return HttpResponse(status=400)
	return HttpResponse(status=200)