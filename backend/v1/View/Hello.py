from django.http import JsonResponse
from rest_framework.views import APIView


class HelloView(APIView):
    def get(self, request):
        return JsonResponse({"message": "Hello, world!"})
