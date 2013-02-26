from django.shortcuts import render
import subprocess

def home(request):
	context = 'dummy context'
	return render(request,'index.html', context)

def shutdown(request):
	subprocess.call(["shutdown.exe", "-f", "-s", "-t", "0"])

