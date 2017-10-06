from django.contrib import admin

# Register your models here.
from django.contrib.contenttypes.admin import GenericStackedInline

from like.models import Like

admin.site.register(Like)


class LikesInline(GenericStackedInline):

    model = Like
    ct_field = 'content_type'
    ct_fk_field = 'object_id'


class LikeAbleAdmin(admin.ModelAdmin):
    inlines = (LikesInline,)
