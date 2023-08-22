from django.http import JsonResponse
from rest_framework.views import APIView

from v1.Controller import ReviewController


class ReviewView(APIView):
    def get(self, request):
        token = None
        review_id = None
        product_id = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if 'review_id' in request.GET:
            review_id = request.GET['review_id']
        if 'product_id' in request.GET:
            product_id = request.GET['product_id']
        if review_id and product_id:
            response_content, status_code = ReviewController.get_review(token, review_id, product_id)
        elif product_id:
            response_content, status_code = ReviewController.get_reviews_for_product(token, product_id)
        elif review_id:
            response_content, status_code = ReviewController.get_review_by_id(token, review_id)
        else:
            response_content, status_code = ReviewController.get_reviews(token)

        return JsonResponse(response_content, status=status_code)

    def post(self, request):
        if 'Authorization' not in request.headers:
            return JsonResponse({'message': 'Unauthorized'}, status=401)
        token = request.headers['Authorization']
        product_id = request.POST['product_id']
        review = request.POST['review']
        rating = request.POST['rating']
        response_content, status_code = ReviewController.create_review(token, product_id, review, rating)
        return JsonResponse(response_content, status=status_code)

    def put(self, request):
        if 'Authorization' not in request.headers:
            return JsonResponse({'message': 'Unauthorized'}, status=401)
        token = request.headers['Authorization']
        review_id = request.GET['id']
        review = request.POST['review']
        rating = request.POST['rating']
        response_content, status_code = ReviewController.update_review(token, review_id, review, rating)
        return JsonResponse(response_content, status=status_code)

    def delete(self, request):
        if 'Authorization' not in request.headers:
            return JsonResponse({'message': 'Unauthorized'}, status=401)
        token = request.headers['Authorization']
        review_id = request.GET['id']
        response_content, status_code = ReviewController.toggle_review_visibility(token, review_id)
        return JsonResponse(response_content, status=status_code)
