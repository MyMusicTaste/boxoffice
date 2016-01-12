from django.contrib import auth
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User

from rest_framework import serializers


@api_view(['GET', 'POST'])
def authorization(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username:
            if password:
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    print('ss')
                    token_model = Token.objects.filter(user_id=user.id)
                    if token_model.exists():
                        serializer = TokenSerializer(token_model, many=True, read_only=True)
                        return Response(serializer.data)
                    else:
                        return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Token
        fields = ('key', 'user')

