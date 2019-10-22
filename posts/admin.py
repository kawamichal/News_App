from django.contrib import admin

from posts.models import Post, Comment


@admin.register(Post)  # same as: admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):  # overwriting default admin page for Post model
    list_display = ('title', 'author', 'publish_date', 'status')
    ordering = ('status', 'publish_date') # sort by status first, then by pub date
    date_hierarchy = "publish_date" # nav bar that sorts according to publish date
    # adding a search bar
    search_fields = ('title', 'text')
    # adding a filter list
    list_filter = ('status', 'author', 'publish_date')
    # pre-adjusted fields in new posts
    prepopulated_fields = {'slug': ('title',)} #authomatically fills the slug field with the name of the post

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ('author', 'post', 'publish_date', 'active')
    list_filter = ('active', 'publish_date')
    search_fields = ('author', 'text')