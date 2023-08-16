from rest_framework.authtoken.models import Token

from user_management.Serializer import UserSerializer
from user_management.Model import UserModel


def logout(token):
    """
        Receives the auth token in the header
        Returns a 200 if the token is valid and the user has been logged out
        Returns a 403 if the token is invalid
    """
    if not token:
        return {'message': 'No token provided'}, 403
    try:
        token = Token.objects.get(key=token)
        token.delete()
        return {'message': 'Logged out'}, 200
    except Token.DoesNotExist:
        return {'message': 'Invalid token'}, 403


def login(username, password):
    """
        Receives the username and password in the body
        Returns a 200 and the access token if the username and password are valid and the user has been logged in
        Returns a 403 if the username and password are invalid
    """
    from django.contrib.auth import authenticate
    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return {'message': 'Logged in!', 'token': token.key, 'user': UserSerializer(user).data}, 200
    else:
        return {'message': 'Invalid username or password'}, 403


def register(email, username, password):
    """
        Receives the email, username and password in the body
        Returns a 201 and the account if the account has been created
        Returns a 409 if the username and/or the email are already taken
    """
    if UserModel.objects.filter(username=username).exists():
        return {'message': 'Username already taken'}, 409
    if UserModel.objects.filter(email=email).exists():
        return {'message': 'Email already taken'}, 409
    user = UserModel.objects.create_user(username=username, email=email, password=password)
    user.save()
    return {'message': 'Account created!', 'user': UserSerializer(user).data}, 201


def delete(token):
    """
        Receives the auth token in the header
        Returns a 200 if the token is valid and the account has been deactivated
        Returns a 403 if the token is invalid
    """
    if not token:
        return {'message': 'No token provided'}, 403
    try:
        token = Token.objects.get(key=token)
        user = token.user
        user.is_active = False
        user.save()
        token.delete()
        return {'message': 'Account deleted'}, 200
    except Token.DoesNotExist:
        return {'message': 'Invalid token'}, 403
