from django.urls import path

from user_management.v1.View import UserView as UserViewV1
from user_management.v2.View import UserView as UserViewV2

urlpatterns = [
    path(r'v1', UserViewV1.as_view(), name='user'),
    path(r'v2', UserViewV2.as_view(), name='user')
]
