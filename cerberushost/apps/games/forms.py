from django import forms
import categories

class GameSubmitForm(forms.Form):
	title = forms.CharField(max_length=100)
	package_file = forms.FileField(label='Select package file',
		help_text='The file MUST be a compressed zip file')
	category = forms.ModelChoiceField(categories.models.Category.objects.all())
	square_icon = forms.FileField(label='Package icon',
		help_text='Icon has to be an image file, preferrably 100x100px. Can be left blank.',
		required=False)
	caption_picture = forms.FileField (label='Caption picture',
		help_text='Caption picture is used in your package home page. Can be left blank.',
		required=False)
	version = forms.CharField(max_length=10)

	