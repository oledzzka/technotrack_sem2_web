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
        return super(CommentViewSet, self).get_queryset().filter(author=self.request.user)
