from django.urls import path

from user_management.View import UserView

urlpatterns = [
    path(r'', UserView.as_view(), name='user'),
]
