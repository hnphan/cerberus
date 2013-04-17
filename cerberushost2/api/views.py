from api.models import Package
from api.serializers import PackageSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly

from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'packages': reverse('package-list', request=request, format=format)
    })


class PackageList(generics.ListCreateAPIView):
    """
    List all packages, or create a new package
    """
    model = Package
    serializer_class = PackageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.developer = self.request.user


class PackageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a package.
    """
    model = Package
    serializer_class = PackageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    
    def pre_save(self, obj):
        obj.developer = self.request.user


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer


class UserInstance(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer