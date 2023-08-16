from django.http import JsonResponse
from rest_framework.views import APIView


class UserView(APIView):
    def get(self, request):
        # logout
        return JsonResponse({'message': 'TODO: logout', 'request': str(request.query_params)})

    def post(self, request):
        # login
        return JsonResponse({'message': 'TODO: login', 'request': str(request.data)})

    def put(self, request):
        # register
        return JsonResponse({'message': 'TODO: register', 'request': str(request.data)})

    def delete(self, request):
        # delete
        return JsonResponse({'message': 'TODO: pause account', 'request': str(request.query_params)})
