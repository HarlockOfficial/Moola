from user_management.v1.Controller import UserController
from v1.Model import ReviewModel, ProductModel
from v1.Serializer import ReviewSerializer


def get_review(token, review_id, product_id):
    """
    Get a review by review_id and product_id
    :param token: The token of the user
    :param review_id: The id of the review
    :param product_id: The id of the product
    :return: A tuple containing the response content and the status code
    """
    if token:
        user_search_content, user_search_status_code = UserController.get_user(token)
        if user_search_status_code == 200 and user_search_content['user'].is_staff:
            try:
                review = ReviewModel.objects.get(id=review_id, product_id=product_id)
                return {'message': 'Review Found!', 'review': ReviewSerializer(review).data}, 200
            except Exception as e:
                return {'message': 'Review Not Found!', 'error': str(e)}, 404
    try:
        review = ReviewModel.objects.get(id=review_id, product_id=product_id, is_active=True)
        return {'message': 'Review Found!', 'review': ReviewSerializer(review).data}, 200
    except Exception as e:
        return {'message': 'Review Not Found!', 'error': str(e)}, 404


def get_reviews_for_product(token, product_id):
    """
    Get all reviews for a product
    :param token: The token of the user
    :param product_id: The id of the product
    :return: A tuple containing the response content and the status code
    """
    if token:
        user_search_content, user_search_status_code = UserController.get_user(token)
        if user_search_status_code == 200 and user_search_content['user'].is_staff:
            try:
                reviews = ReviewModel.objects.filter(product_id=product_id)
                return {'message': 'Reviews Found!', 'reviews': ReviewSerializer(reviews, many=True).data}, 200
            except Exception as e:
                return {'message': 'Reviews Not Found!', 'error': str(e)}, 404
    try:
        reviews = ReviewModel.objects.filter(product_id=product_id, is_active=True)
        return {'message': 'Reviews Found!', 'reviews': ReviewSerializer(reviews, many=True).data}, 200
    except Exception as e:
        return {'message': 'Reviews Not Found!', 'error': str(e)}, 404


def get_review_by_id(token, review_id):
    """
    Get a review by review_id
    :param token: The token of the user
    :param review_id: The id of the review
    :return: A tuple containing the response content and the status code
    """
    if token:
        user_search_content, user_search_status_code = UserController.get_user(token)
        if user_search_status_code == 200 and user_search_content['user'].is_staff:
            try:
                review = ReviewModel.objects.get(id=review_id)
                return {'message': 'Review Found!', 'review': ReviewSerializer(review).data}, 200
            except Exception as e:
                return {'message': 'Review Not Found!', 'error': str(e)}, 404
    try:
        review = ReviewModel.objects.get(id=review_id, is_active=True)
        return {'message': 'Review Found!', 'review': ReviewSerializer(review).data}, 200
    except Exception as e:
        return {'message': 'Review Not Found!', 'error': str(e)}, 404


def get_reviews(token):
    """
    Get all reviews
    :param token: The token of the user
    :return: A tuple containing the response content and the status code
    """
    if token:
        user_search_content, user_search_status_code = UserController.get_user(token)
        if user_search_status_code == 200 and user_search_content['user'].is_staff:
            try:
                reviews = ReviewModel.objects.all()
                return {'message': 'Reviews Found!', 'reviews': ReviewSerializer(reviews, many=True).data}, 200
            except Exception as e:
                return {'message': 'Reviews Not Found!', 'error': str(e)}, 404
    try:
        reviews = ReviewModel.objects.filter(is_active=True)
        return {'message': 'Reviews Found!', 'reviews': ReviewSerializer(reviews, many=True).data}, 200
    except Exception as e:
        return {'message': 'Reviews Not Found!', 'error': str(e)}, 404


def create_review(token, product_id, review, rating):
    """
    Create a review
    :param token: The token of the user
    :param product_id: The id of the product
    :param review: The review
    :param rating: The rating
    :return: A tuple containing the response content and the status code
    """
    if not token:
        return {'message': 'Unauthorized'}, 401
    user_search_content, user_search_status_code = UserController.get_user(token)
    if user_search_status_code != 200:
        return user_search_content, user_search_status_code
    try:
        product = ProductModel.objects.get(id=product_id)
        review = ReviewModel.objects.create(user=user_search_content, product=product, review=review, rating=rating)
        return {'message': 'Review Created!', 'review': ReviewSerializer(review).data}, 201
    except Exception as e:
        return {'message': 'Review Not Created!', 'error': str(e)}, 400


def update_review(token, review_id, review_content, rating):
    """
    Update a review
    :param token: The token of the user
    :param review_id: The id of the review
    :param review_content: The review
    :param rating: The rating
    :return: A tuple containing the response content and the status code
    """
    if not token:
        return {'message': 'Unauthorized'}, 401
    user_search_content, user_search_status_code = UserController.get_user(token)
    if user_search_status_code != 200:
        return user_search_content, user_search_status_code
    try:
        review = ReviewModel.objects.get(id=review_id)
        if not user_search_content['user'].is_staff and user_search_content['user'] != review.user:
            return {'message': 'Unauthorized'}, 401
        review.review = review_content
        review.rating = rating
        review.updated_by = user_search_content['user']
        review.save()
        return {'message': 'Review Updated!', 'review': ReviewSerializer(review_content).data}, 200
    except Exception as e:
        return {'message': 'Review Not Updated!', 'error': str(e)}, 400


def toggle_review_visibility(token, review_id):
    """
    Toggle the visibility of a review
    :param token: The token of the user
    :param review_id: The id of the review
    :return: A tuple containing the response content and the status code
    """
    if not token:
        return {'message': 'Unauthorized'}, 401
    user_search_content, user_search_status_code = UserController.get_user(token)
    if user_search_status_code != 200:
        return user_search_content, user_search_status_code
    try:
        review = ReviewModel.objects.get(id=review_id)
        if not user_search_content['user'].is_staff and user_search_content['user'] != review.user:
            return {'message': 'Unauthorized'}, 401
        review.is_active = not review.is_active
        review.updated_by = user_search_content['user']
        review.save()
        return {'message': 'Review Visibility Toggled!', 'review': ReviewSerializer(review).data}, 200
    except Exception as e:
        return {'message': 'Review Visibility Not Toggled!', 'error': str(e)}, 400
