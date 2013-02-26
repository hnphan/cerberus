from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.ForeignKey(User, editable=True)
    class Meta:
        abstract = True

class Package(models.Model):
	pid = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	developer = models.ForeignKey(User, related_name='packages')
	location = models.CharField(max_length=200)
	
	class Meta:
		ordering = ('title',)

	def __unicode__(self):
		return self.title



