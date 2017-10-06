from django.shortcuts import render

from rest_framework import viewsets, permissions

from like.models import Like
from like.serializer import LikeSerializer
from core.permissions import IsOwnerOrReadOnly


class LikeSetView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = permissions.IsAuthenticated, IsOwnerOrReadOnly,

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super(LikeSetView, self).get_queryset()
        if self.request.query_params.get('username'):
            qs = qs.filter(author__username=self.request.query_params.get('username'))
        return qs
