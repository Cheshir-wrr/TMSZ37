from django.contrib import admin

from applications.blog.models import Comments
from applications.blog.models import Post


@admin.register(Post)
class PostAdminModel(admin.ModelAdmin):
    pass


@admin.register(Comments)
class CommentAdminModel(admin.ModelAdmin):
    pass


# class Comment(admin.ModelAdmin):
#     list_display = ('name', 'email', 'post', 'created', 'active')
#     list_filter = ('active', 'created', 'updated')
#     search_fields = ('name', 'email', 'body')
#
#
# admin.site.register(Comment, Comment)
