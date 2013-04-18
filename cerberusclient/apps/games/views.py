from django.shortcuts import render
from apps.system.models import LocalPackage
from django.http import HttpResponse


# Create your views here.
def home(request):
	installed_packages = LocalPackage.objects.filter(status=2)
	return render(request,'games/index.html', {'packages':installed_packages, 'title': "installed games"})

def package_action(request, package_id):
	if request.GET['command'] == "start":
		try:
			package = LocalPackage.objects.get(pk=package_id)
			# go to package local path

			# look for command text file

			# launch the command

			
		except:
			return HttpResponse(status=400)
	return HttpResponse(status=200)