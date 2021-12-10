from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer,LoginSerializer 
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login,logout


#from django.core.exceptions import ImproperlyConfigured
#from rest_framework import views
#from rest_framework.decorators import action
#from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


# User Registration
class RegisterAPIView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

#User Login
class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request,format=None):
        data = request.data

        email = data.get('email',None)
        password = data.get('password',None)

        user = authenticate(username=email,password=password)

        if user is not None and user.is_active:
            return Response(status=status.HTTP_200_OK)
               
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)            













