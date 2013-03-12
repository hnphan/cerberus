from django.db import models

# Create your models here.
class Message(models.Model):
	content = models.TextField(max_length=1000)
	seen = models.BooleanField()
	timestamp = models.DateTimeField()


	def __unicode__(self):
		return self.content