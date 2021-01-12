"""roomReservationBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getDocumentsDetails, name = 'document')
]

# from django.urls import path, include
# from django.contrib.auth.models import User
# from rest_framework import serializers, viewsets, routers
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']


# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     def get(self):
#         print('hi')
#         return 'hi'

# @api_view(['GET', 'POST'])
# def getDocumentsDetail(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'POST':
#         # serializer = SnippetSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response( "hi") #serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Routers provide a way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', getDocumentsDetail)


# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls))
# ]