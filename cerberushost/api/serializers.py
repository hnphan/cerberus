from django.contrib.auth.models import User, Group, Permission
from api.models import Package, User
from rest_framework import serializers


class PackageSerializer(serializers.HyperlinkedModelSerializer):
    developer = serializers.Field(source='developer.username')
    pid = serializers.Field()

    class Meta:
        model = Package
        fields = ('pid','url', 'title', 'developer', 'package_file','square_icon','version')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    packages =  serializers.ManyHyperlinkedRelatedField(view_name='package-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'packages')



