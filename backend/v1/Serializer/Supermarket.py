from rest_framework.serializers import ModelSerializer

from user_management.Serializer import UserSerializer
from v1.Model import Supermarket


class SupermarketSerializer(ModelSerializer):
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    class Meta:
        model = Supermarket
        fields = '__all__'