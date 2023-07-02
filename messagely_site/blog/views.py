from django.shortcuts import render
from django.db.models import Count
from . import models

def home(request):
    """
    The Blog Homepage
    """
    latest_posts = models.Post.objects.order_by('published').reverse()[:10]
    mess_topics = models.Topic.objects.annotate(total_posts = Count('blog_posts')).values('name', 'total_posts')
    topics = mess_topics.order_by('total_posts').reverse()
    context = {'latest_posts': latest_posts, 'topics': topics}
    return render(request, 'blog/home.html', context)