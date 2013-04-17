from system.models import Message, LocalPackage
from django.contrib import admin

class MessageAdmin(admin.ModelAdmin):
	list_display = ('timestamp', 'content', 'seen')

admin.site.register(Message,MessageAdmin)

class LocalPackageAdmin(admin.ModelAdmin):
	list_display = ('title', 'developer', 'version')

admin.site.register(LocalPackage,LocalPackageAdmin)