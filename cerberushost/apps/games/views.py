from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import GameSubmitForm
from api import models
from categories import models as cmodels

# Create your views here.
def home(request):
	return


def submitGame(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = GameSubmitForm(request.POST, request.FILES)
			if form.is_valid():
				# Process the data
				newgame = models.Package(title=request.POST['title'],
					developer = request.user,
					package_file = request.FILES['package_file'],
					category = cmodels.Category.objects.get(pk=request.POST['category']),
					#square_icon=request.FILES['square_icon'],
					#caption_picture=request.FILES['caption_picture'],
					version=request.POST['version'])
				newgame.save()

				return HttpResponseRedirect('/')
		else:
			form = GameSubmitForm()
		return render(request, "games/submit.html", {'form': form})
	else:
		return HttpResponseRedirect('/accounts/login/')