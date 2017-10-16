from django.shortcuts import render

# Create your views here.
from django.db.models.query import QuerySet
from rest_framework import viewsets, permissions

from core.permissions import IsOwnerOrReadOnly
from event.models import Event
from event.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        if self.request.query_params.get('user_id'):
            return super(EventViewSet, self).get_queryset().all().filter(author__in=self.request.user.sub_users.all())
        else:
            return None
