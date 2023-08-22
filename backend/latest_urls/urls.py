
from django.urls import path, include

urlpatterns = [
    path(r'user/', include('user_management.urls')),
    path(r'v1/', include('v1.urls')),
]
