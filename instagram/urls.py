"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from rest_framework.authtoken import views

from post import views as post_views
from like import views as like_views
from core import views as core_views
from comment import views as comment_views
from event import views as event_view

router = routers.DefaultRouter()
router.register(r'post', post_views.PostViewSet)
router.register(r'like', like_views.LikeSetView)
router.register(r'user', core_views.SelfUserViewSet)
router.register(r'other_user', core_views.OtherUserViewSet)
router.register(r'sub_user', core_views.SubscriptionsViewSet)
router.register(r'comment', comment_views.CommentViewSet)
router.register(r'event', event_view.EventViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^social/', include('social_django.urls', namespace='social')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
]