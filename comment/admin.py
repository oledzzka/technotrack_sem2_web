from django.contrib import admin

# Register your models here.
from django.contrib.contenttypes.admin import GenericStackedInline

from comment.models import Comment
from like.admin import LikeAbleAdmin


class CommentsInline(GenericStackedInline):

    model = Comment
    ct_field = 'content_type'
    ct_fk_field = 'object_id'


class CommentAbleAdmin(admin.ModelAdmin):
    inlines = (CommentsInline,)


@admin.register(Comment)
class CommentAdmin(LikeAbleAdmin):
    readonly_fields = ('content_object', 'likes_count')
    exclude = ('object_id', 'content_type', )


