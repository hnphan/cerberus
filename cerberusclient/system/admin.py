from system.models import Message
from django.contrib import admin

class MessageAdmin(admin.ModelAdmin):
	list_display = ('timestamp', 'content', 'seen')

admin.site.register(Message,MessageAdmin)