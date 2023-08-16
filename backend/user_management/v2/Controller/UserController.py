import os

from django.template import loader
from rest_framework.authtoken.models import Token

from user_management.Model import UserModel
from user_management.Serializer import UserSerializer


def create_user(email):
    """
        Create a new user with the given email
        The password will be sent to the user's email

        Returns a 201 and the account if the account has been created
        Returns a 409 if the email is already taken
    """
    try:
        UserModel.objects.get(email=email)
        return {'message': 'User already exists'}, 409
    except UserModel.DoesNotExist:
        password = UserModel.objects.make_random_password()
        user = UserModel.objects.create_user(email=email, username=email, password=password)
        message = loader.render_to_string('email/register.html',
                                          {
                                              'subject': os.getenv('REGISTER_EMAIL_SUBJECT'),
                                              'username': email,
                                              'password': password
                                          })
        user.email_user(subject=os.getenv('EMAIL_SUBJECT'), message=message, html_message=message)
        user.save()
        return {'message': 'Account created!', 'user': UserSerializer(user).data}, 201


def update_user(token, updated_data):
    """
        Update a user's username and or password
        The user must be logged in to update their username or password

        Returns a 200 and the user if the user is updated
        Returns a 400 if the user is not logged in
        Returns a 409 if the username is already taken

        After the process is complete, the user will be logged out
    """
    try:
        user = UserModel.objects.get(auth_token=token)
        if 'username' in updated_data:
            if UserModel.objects.filter(username=updated_data['username']).exists():
                return {'message': 'Username already taken'}, 409
            user.username = updated_data['username']
        if 'password' in updated_data:
            user.set_password(updated_data['password'])
        user.save()
        token = Token.objects.get(user=user)
        token.delete()
        return {'message': 'User updated!', 'user': UserSerializer(user).data}, 200
    except UserModel.DoesNotExist:
        return {'message': 'User is not logged in'}, 400