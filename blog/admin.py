from django.contrib import admin
from .models import Post, PostCategory
# from django_jalali.admin.filters import JDateFieldListFilter
# import django_jalali.admin as jadmin

class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'post_category', 'pub_date', 'last_modified', 'author']
    list_filter = [
        # ('pub_date', JDateFieldListFilter), #TODO : Fix jalali date filter error
        'author',
        'post_category'
    ]
    prepopulated_fields = { 'slug': ('name',) }
    search_fields = ['name', 'content']

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = { 'slug': ('name',) }

admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
