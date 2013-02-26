from django.db import models

# Create your models here.
class Package(models.Model):
	pid = models.PositiveIntegerField() #packageid from online db
	title = models.CharField(max_length=200)
	developer = models.CharField(max_length=200)
	location = models.FilePathField()
	download_status = models.PositiveIntegerField()
	installed = models.BooleanField()

	class Meta:
		ordering = ('title',)

	def __unicode__(self):
		return self.title