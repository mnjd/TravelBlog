from rest_framework.generics import ListAPIView
from articles.models import Articles
from .serializers import PostSerializer

class PostListAPIView(ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = PostSerializer

