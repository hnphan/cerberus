from django.db import models

# System message for notification bar
class Message(models.Model):
	content = models.TextField(max_length=1000)
	seen = models.BooleanField()
	timestamp = models.DateTimeField()


	def __unicode__(self):
		return self.content


# Installed packages
class LocalPackage(models.Model):
	pid = models.PositiveIntegerField() #packageid from online db
	title = models.CharField(max_length=200)
	developer = models.CharField(max_length=200)
	location = models.CharField(max_length=1000) #local path
	download_status = models.PositiveIntegerField()
	version = models.CharField(max_length=10)
	# status = 0: attempted to download but not finish
	# status = 1: download finished but not installed
	# status = 2: installed
	status = models.PositiveIntegerField()
	iconFile = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title