from api.models import UserData, Package
from django.contrib import admin

class PackageAdmin(admin.ModelAdmin):
	list_display = ('title', 'developer')

admin.site.register(Package,PackageAdmin)
