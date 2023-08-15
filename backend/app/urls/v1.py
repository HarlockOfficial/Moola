from django.urls import path

from app.view import HelloView

urlpatterns = [
    path(r'hello', HelloView.as_view(), name='hello'),
]