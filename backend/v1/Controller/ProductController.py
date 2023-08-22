from user_management.v1.Controller import UserController
from v1.Model import ProductModel
from v1.Serializer import ProductSerializer


def create_product(name, description, image, created_by):
    try:
        product = ProductModel(name=name, description=description, image=image, created_by=created_by)
        product.save()
        return {'message': 'Product Created!', 'product': ProductSerializer(product).data}, 201
    except Exception as e:
        return {'message': 'Product Creation Failed!', 'error': str(e)}, 400


def update_product(product_id, name, description, image, updated_by):
    try:
        product = ProductModel.objects.get(id=product_id)
        if not (updated_by.is_staff or updated_by.id == product.created_by.id):
            return {'message': 'Unauthorized!'}, 401
        product.name = name
        product.description = description
        product.image = image
        product.updated_by = updated_by
        product.save()
        return {'message': 'Product Updated!', 'product': ProductSerializer(product).data}, 200
    except Exception as e:
        return {'message': 'Product Update Failed!', 'error': str(e)}, 400


def toggle_product_visibility(product_id, deleted_by):
    try:
        product = ProductModel.objects.get(id=product_id)
        if not (deleted_by.is_staff or deleted_by.id == product.created_by.id):
            return {'message': 'Unauthorized!'}, 401
        product.is_active = not product.is_active
        product.deleted_by = deleted_by
        product.save()
        return {'message': 'Product Visibility Changed!'}, 200
    except Exception as e:
        return {'message': 'Product Visibility Change Failed!', 'error': str(e)}, 400


def get_product(token, product_id):
    try:
        product = None
        if token:
            user_search_content, user_search_status_code = UserController.get_user(token)
            if user_search_status_code == 200 and user_search_content['user'].is_staff:
                product = ProductModel.objects.get(id=product_id)
        if not product:
            product = ProductModel.objects.get(id=product_id, is_active=True)
        return {'message': 'Product Found!', 'product': ProductSerializer(product).data}, 200
    except Exception as e:
        return {'message': 'Product Not Found!', 'error': str(e)}, 404


def get_products(token):
    try:
        products = None
        if token:
            user_search_content, user_search_status_code = UserController.get_user(token)
            if user_search_status_code == 200 and user_search_content['user'].is_staff:
                products = ProductModel.objects.all()
        if not products:
            products = ProductModel.objects.filter(is_active=True)
        return {'message': 'Products Found!', 'products': ProductSerializer(products, many=True).data}, 200
    except Exception as e:
        return {'message': 'Products Not Found!', 'error': str(e)}, 404
