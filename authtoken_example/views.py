from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from authtoken_example import serializers
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout as auth_logout

class LoginView(APIView):
    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status.HTTP_200_OK)


class LogOutView(APIView):

    def post(self, request):
        auth_logout(request)
        return Response(status_code=204)
