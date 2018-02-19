from rest_framework.serializers import ModelSerializer
from articles.models import Articles

class PostSerializer(ModelSerializer):
    class Meta:
        model = Articles
        fields = [
                'title',
                'body',
                'author',
                'created_at',
                'updated_at',
                ]

