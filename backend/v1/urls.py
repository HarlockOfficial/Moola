from django.urls import path

from v1.View import HelloView, ProductView

urlpatterns = [
    path(r'hello', HelloView.as_view(), name='hello'),
    path(r'product', ProductView.as_view(), name='product'),
]
