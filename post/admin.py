from django.contrib import admin

# Register your models here.
from comment.admin import CommentAbleAdmin
from like.admin import LikeAbleAdmin
from post.models import Post


@admin.register(Post)
class PostAdmin(LikeAbleAdmin, CommentAbleAdmin):
    inlines = CommentAbleAdmin.inlines + LikeAbleAdmin.inlines
    readonly_fields = 'likes_count',
