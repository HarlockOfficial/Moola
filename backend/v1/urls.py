from django.urls import path

from v1.View import HelloView

urlpatterns = [
    path(r'hello', HelloView.as_view(), name='hello'),
]
