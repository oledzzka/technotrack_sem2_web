from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from core.permissions import IsOwnerOrReadOnly
from event.models import Event
from event.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        qs = []
        for event in super(EventViewSet, self).get_queryset().all():
            # if event.author in self.request.user.sub_users.all():
               qs.append(event)
        return {Event: qs}
