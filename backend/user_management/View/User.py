from django.http import JsonResponse
from rest_framework.views import APIView


class UserView(APIView):
    def get(self):
        # logout
        return JsonResponse({'message': 'TODO: logout'})

    def post(self):
        # login
        return JsonResponse({'message': 'TODO: login'})

    def put(self):
        # register
        return JsonResponse({'message': 'TODO: register'})

    def delete(self):
        # delete
        return JsonResponse({'message': 'TODO: pause account'})
