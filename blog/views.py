from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, PostCategory
from django.conf import settings

# Show all posts in /blog/
def posts(request):
    posts_list = Post.objects.order_by('-id')
    paginator = Paginator(posts_list, 2)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    categories = []
    for i in PostCategory.objects.all():
        categories.append(i)

    context = { 'posts': posts, 'categories': categories }
    return render(request, 'blog/posts.html', context)

# Show specific post with slug like /blog/post_slug
def detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    post.media_url = settings.MEDIA_URL
    context = { 'post': post }
    return render(request, 'blog/detail.html', context)

# Show posts list by category
def list_category(request, cat_slug):
    posts_list = Post.objects.all().filter(post_category__slug=cat_slug)
    paginator = Paginator(posts_list, 2)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    categories = []
    for i in PostCategory.objects.all():
        categories.append(i)

    context = { 'posts': posts, 'categories': categories }
    return render(request, 'blog/posts.html', context)
