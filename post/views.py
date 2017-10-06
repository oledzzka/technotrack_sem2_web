# Create your views here.
from rest_framework import viewsets, permissions

from core.permissions import IsOwnerOrReadOnly
from post.models import Post
from post.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super(PostViewSet, self).get_queryset()
        if self.request.query_params.get('user_id'):
            qs = qs.filter(author__id=self.request.query_params.get('user_id'))
            if len(qs) != 0 and qs.all()[0].author not in self.request.user.subscriptions.all():
                qs = None
        else:
            qs = super(PostViewSet, self).get_queryset().filter(author=self.request.user)
        return qs
