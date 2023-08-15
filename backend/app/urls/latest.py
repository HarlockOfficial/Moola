from django.urls import path, include

urlpatterns = [
    path(r'v1/', include('app.urls.v1')),
]