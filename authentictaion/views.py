from http.client import HTTP_PORT
import imp
from os import stat_result
from sre_constants import SUCCESS
from telnetlib import STATUS
from urllib.request import HTTPBasicAuthHandler
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response

# Create your views here.
class HellpAuthView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={"message":"Hello Auth"},status=status.HTTP_200_OK)



