# Create your views here.
from django.views.generic import TemplateView

from rest_framework import viewsets

from core.models import User
from core.serializers import SelfUserSerializer, OtherUserSerializer, SubscriptionSerializer


class SelfUserViewSet(viewsets.ModelViewSet):
    serializer_class = SelfUserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        qs = super(SelfUserViewSet, self).get_queryset().filter(id=self.request.user.id)
        return qs


class OtherUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OtherUserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        qs = super(OtherUserViewSet, self).get_queryset()
        # if self.request.query_params.get('id'):
        #     qs = qs.filter(id=self.request.query_params.get('id'))
        return qs


class SubscriptionsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = User.sub_users.through.objects.all()

    def get_queryset(self):
        return super(SubscriptionsViewSet, self).get_queryset().filter(from_user_id=self.request.user.id)


class IndexView(TemplateView):
    template_name = "index.html"
