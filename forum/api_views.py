from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .models import Post
from .serializers import PostSerializer


class PostPagePaginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PostPagePaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        thread_id = self.kwargs['thread_id']
        return Post.objects.filter(thread_id=thread_id).order_by('created_at')
