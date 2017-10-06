from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from comment.models import Comment
from comment.serializers import CommentSerializer
from core.permissions import IsOwnerOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super(CommentViewSet, self).get_queryset()
        if self.request.query_params.get('user_id'):
            qs = qs.filter(author__id=self.request.query_params.get('user_id'))
            if len(qs) != 0 and qs.all()[0].author not in self.request.user.subscriptions.all():
                qs = None
        else:
            qs = super(CommentViewSet, self).get_queryset().filter(author=self.request.user)
        return qs