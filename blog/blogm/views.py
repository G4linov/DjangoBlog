from datetime import datetime

from django.shortcuts import render
from django.template.defaultfilters import title
from unicodedata import category

from .models import Post, Category

CURRENT_DATE = datetime.now()

def index(request):

    post_list = Post.objects.select_related(
        'category'
    ).filter(
        category__is_published=True,
        is_published=True,
        pub_date__lt=CURRENT_DATE,
    )
    posts = {
        'post_list' : post_list,
    }
    return render(request, 'blogm/index.html', posts)

def post_detail(request, post_id):
    post_details = Post.objects.get(id=post_id)
    post_context = {'post': post_details}
    return render(request, 'blogm/detail.html', post_context)

def category_posts(request, category_slug):
    post_list = Post.objects.select_related(
        'category'
    ).filter(
        category__slug=category_slug,
        category__is_published=True,
        pub_date__lt=CURRENT_DATE
    )
    category_db = Category.objects.get(slug=category_slug)
    category_context = {
        'category' : category_db,
        'post_list' : post_list,
    }
    return render(request, 'blogm/category.html', category_context)
