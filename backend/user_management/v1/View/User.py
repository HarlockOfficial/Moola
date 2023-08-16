from django.http import JsonResponse
from rest_framework.views import APIView

from user_management.v1.Controller import UserController


class UserView(APIView):
    def get(self, request):
        # logout
        """
            Receives the auth token in the header
            Returns a 200 if the token is valid and the user has been logged out
            Returns a 403 if the token is invalid
        """
        response_content, response_code = UserController.logout(request.headers['Authorization'])
        return JsonResponse(response_content, status=response_code)

    def post(self, request):
        # login
        """
            Receives the username and password in the body
            Returns a 200 and the access token if the username and password are valid and the user has been logged in
            Returns a 403 if the username and password are invalid
        """
        response_content, response_code = UserController.login(request.data['username'], request.data['password'])
        response = JsonResponse(response_content, status=response_code)
        if 'token' in response_content.keys():
            response['Authorization'] = response_content['token']
        return response

    def put(self, request):
        # register
        """
            Receives the email, username and password in the body
            Returns a 201 and the account if the account has been created
            Returns a 409 if the username and/or the email are already taken
        """
        response_content, response_code = UserController.register(request.data['email'], request.data['username'],
                                                                  request.data['password'])
        return JsonResponse(response_content, status=response_code)

    def delete(self, request):
        # delete
        """
            Receives the auth token in the header
            Returns a 200 if the token is valid and the account has been deleted
            Returns a 403 if the token is invalid
        """
        response_content, response_code = UserController.delete(request.headers['Authorization'])
        return JsonResponse(response_content, status=response_code)
