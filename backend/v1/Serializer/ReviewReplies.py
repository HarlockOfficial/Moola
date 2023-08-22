from rest_framework.serializers import ModelSerializer

from user_management.Serializer import UserSerializer
from v1.Model import ReviewRepliesModel
from v1.Serializer import ReviewSerializer


class ReviewRepliesSerializer(ModelSerializer):
    review = ReviewSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = ReviewRepliesModel
        fields = ('id', 'review', 'other_reply', 'user', 'reply', 'created_at', 'updated_at', 'is_active')

    def get_other_reply(self, obj):
        if obj.other_reply is not None:
            return ReviewRepliesSerializer(obj.other_reply).data
        return None