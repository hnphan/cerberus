from django.shortcuts import render

def home(request):
	context = 'dummy context'
	return render(request,'index.html', context)



