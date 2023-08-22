from django.http import JsonResponse
from rest_framework.views import APIView

from user_management.v1.Controller import UserController
from v1.Controller import ProductController


class ProductView(APIView):
    def get(self, request):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if 'id' in request.GET:
            response_content, status_code = ProductController.get_product(token, request.GET['id'])
        else:
            response_content, status_code = ProductController.get_products(token)
        return JsonResponse(response_content, status=status_code)

    def post(self, request):
        if 'Authorization' not in request.headers:
            return JsonResponse({'message': 'Unauthorized'}, status=401)

        token = request.headers['Authorization']
        user_search_content, user_search_status_code = UserController.get_user(token)
        if user_search_status_code != 200:
            return JsonResponse(user_search_content, status=user_search_status_code)

        if ('name' not in request.POST or
                'description' not in request.POST or 'image' not in request.FILES):
            return JsonResponse({'message': 'Missing Parameters!'}, status=400)

        name = request.POST['name']
        description = request.POST['description']
        image = request.FILES['image']
        created_by = user_search_content['user']

        response_content, status_code = ProductController.create_product(name, description, image, created_by)

        return JsonResponse(response_content, status=status_code)

    def put(self, request):
        if 'Authorization' not in request.headers:
            return JsonResponse({'message': 'Unauthorized'}, status=401)

        token = request.headers['Authorization']
        user_search_content, user_search_status_code = UserController.get_user(token)
        if user_search_status_code != 200:
            return JsonResponse(user_search_content, status=user_search_status_code)

        if ('id' not in request.GET or 'name' not in request.POST or
                'description' not in request.POST or 'image' not in request.FILES):
            return JsonResponse({'message': 'Missing Parameters!'}, status=400)

        id = request.GET['id']
        name = request.POST['name']
        description = request.POST['description']
        image = request.FILES['image']
        updated_by = user_search_content['user']

        response_content, status_code = ProductController.update_product(id, name, description, image, updated_by)

        return JsonResponse(response_content, status=status_code)

    def delete(self, request):
        if 'Authorization' not in request.headers:
            return JsonResponse({'message': 'Unauthorized'}, status=401)

        token = request.headers['Authorization']
        user_search_content, user_search_status_code = UserController.get_user(token)
        if user_search_status_code != 200:
            return JsonResponse(user_search_content, status=user_search_status_code)

        if 'id' not in request.GET:
            return JsonResponse({'message': 'Missing Parameters!'}, status=400)

        id = request.GET['id']
        deleted_by = user_search_content['user']

        response_content, status_code = ProductController.toggle_product_visibility(id, deleted_by)

        return JsonResponse(response_content, status=status_code)
