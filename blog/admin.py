from django.contrib import admin
from .models import Post, PostCategory

class PostAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']

admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
