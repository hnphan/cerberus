from django.db import models

def get_media_upload_dir(instance, filename):
    user_id  = instance.developer.id
    today = datetime.now()
    now_path = today.strftime("%Y%m%d%H%M%S")
    upload_dir = "%s/%d/%s/%s" % (settings.MEDIA_ROOT, user_id, now_path, filename)
    print "Upload dir set to: %s" % upload_dir
    return upload_dir

# Create your models here.
class Package(models.Model):
	pid = models.PositiveIntegerField() #packageid from online db
	title = models.CharField(max_length=200)
	developer = models.CharField(max_length=200)
	location = models.FilePathField()
	# small thumbnail for displaying in list
	square_icon = models.FileField(upload_to=get_media_upload_dir, blank=True, null=True)
	download_status = models.PositiveIntegerField()
	installed = models.BooleanField()

	class Meta:
		ordering = ('title',)

	def __unicode__(self):
		return self.title