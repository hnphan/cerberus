from django.db import models
from django.contrib.auth.models import User
import categories
from config import settings
from datetime import datetime

def get_media_upload_dir(instance, filename):
    user_id  = instance.developer.id
    today = datetime.now()
    now_path = today.strftime("%Y%m%d%H%M%S")
    upload_dir = "%s/%d/%s/%s" % (settings.MEDIA_ROOT, user_id, now_path, filename)
    print "Upload dir set to: %s" % upload_dir
    return upload_dir


class UserData(models.Model):
    user = models.ForeignKey(User, editable=True)
    class Meta:
        abstract = True

class Package(models.Model):
	pid = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	developer = models.ForeignKey(User, related_name='packages')
	# package zip file
	package_file = models.FileField(upload_to=get_media_upload_dir)
	# small thumbnail for displaying in list
	square_icon = models.FileField(upload_to=get_media_upload_dir, blank=True, null=True)
	# big thumbnail, for decoration in download page
	caption_picture = models.FileField(upload_to=get_media_upload_dir, blank=True, null=True)
	version = models.CharField(max_length=10)
	category = models.ForeignKey('categories.Category')
	download_count = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ('title',)

	def __unicode__(self):
		return self.title
