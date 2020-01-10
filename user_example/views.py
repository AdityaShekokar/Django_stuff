from django.http import HttpResponse
from django.shortcuts import render
from requests import Response
from rest_framework.views import APIView


def index(request):
    return render(request, 'user_example/index.html')
