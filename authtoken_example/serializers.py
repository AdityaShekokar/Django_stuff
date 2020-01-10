from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    breakpoint()
    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "Account is disable."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credential."
                raise exceptions.ValidationError(msg)
            pass
        else:
            msg = "Must provide username and password."
            raise exceptions.ValidationError(msg)
        return data