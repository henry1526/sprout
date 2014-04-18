from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib import auth
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from django.core.context_processors import csrf
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework import generics
from rest_framework import permissions

from django.contrib.auth.models import User
from .models import *
from .serializers import *


# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class UserList(generics.ListCreateAPIView):
    """List all users or create a new User"""
    permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """Retrieve, update or delete a User instance."""
    permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer


# class AddressList(generics.ListCreateAPIView):
#     """List all addresses or create a new Address"""
#     permission_classes = (permissions.IsAuthenticated,)
#     model = Address
#     serializer_class = AddressSerializer


# class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
#     """Retrieve, update or delete an Address."""
#     permission_classes = (permissions.IsAuthenticated,)
#     model = Address
#     serializer_class = AddressSerializer

class ObtainUserAuthToken(ObtainAuthToken):
    '''
    Extend the ObtainAuthToken class as defined by the
    REST Framework. This is so we can do our own authentication
    and build our own response dictionary.
    '''

    def post(self, request):
        '''
        A username and password are POST'ed to this view.
        Here we will check if this username and password has a REST Framework Token
        (which was created in the @receiver of models.py)

        If authenticated, send back the token for the angular app to store as a cookie
        '''

        # Authenticate the email address after its been all lowercased
        email = request.DATA['username']
        lowercase_email = email.lower()
        request.DATA['username'] = lowercase_email

        # read in the data that was sent up from the angular app
        serializer = self.serializer_class(data=request.DATA)

        # Is there a Token connected to this user?
        if serializer.is_valid():
            authenticated_user = serializer.object['user']
            token, created = Token.objects.get_or_create(user=authenticated_user)

            # build a dictionary to send back to the angular app.
            # the key: value pairs listed here will be available to
            # the frontend angular app
            user_response = {
                'id': authenticated_user.id,
                'username': authenticated_user.username,
                'first_name': authenticated_user.first_name,
                'last_name': authenticated_user.last_name,
                'token': token.key
            }

            return Response(user_response)

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


def logout(request):
    auth.logout(request)
    return JSONResponse([{'success': 'Logged out!'}])