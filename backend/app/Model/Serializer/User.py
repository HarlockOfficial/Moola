from rest_framework.serializers import ModelSerializer

from app.Model import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('password', )
