from django.contrib import auth
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import serializers

from rest_framework import authentication
from rest_framework import exceptions


class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        email = request.POST.get('username')

        if not email:
            return None

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)


@api_view(['GET', 'POST'])
@authentication_classes((ExampleAuthentication,))
@permission_classes((IsAuthenticated,))
def authorization(request):
    if request.method == 'POST':
        if request.user:
            user = auth.authenticate(username=request.user.username, password=request.POST.get('password'))
            if user is not None:
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
    token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ('token', 'user')


