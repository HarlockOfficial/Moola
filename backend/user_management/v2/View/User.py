from django.http import JsonResponse
from rest_framework.views import APIView

from user_management.v2.Controller import UserController
from user_management.v1.Controller import UserController as UserControllerV1


class UserView(APIView):
    def post(self, request):
        """
            Create a new user or login an existing user
            If only the email is provided, a new user will be created and the password will be sent to the user's email
            If both the email and password are provided, the user will be logged in and the auth token will be returned

            Returns a 200 and the access token if the username and password are valid and the user has been logged in
            Returns a 201 and the account if the account has been created
            Returns a 400 if the email is not provided
            Returns a 403 if the username and password are invalid
            Returns a 409 if the username and/or the email are already taken
        """
        if 'email' not in request.data:
            return JsonResponse({'message': 'Email is required'}, status=400)
        if 'password' not in request.data:
            response_content, status_code = UserController.create_user(request.data['email'])
        else:
            response_content, status_code = UserControllerV1.login(request.data['email'], request.data['password'])
        response = JsonResponse(response_content, status=status_code)
        if 'token' in response_content.keys():
            response['Authorization'] = response_content['token']
        return response

    def patch(self, request):
        """
            Update a user's username and or password
            The user must be logged in to update their username or password

            Returns 200 if the user is updated
            Returns 400 if the user is not logged in
            Returns 409 if the username is already taken

            After the process is complete, the user will be logged out
        """
        if 'Authorization' not in request.headers:
            return JsonResponse({'message': 'User is not logged in'}, status=400)
        response_content, status_code = UserController.update_user(request.headers['Authorization'], request.data)
        return JsonResponse(response_content, status=status_code)
