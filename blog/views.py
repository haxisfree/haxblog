from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
from django.core.paginator import Paginator
# from . import models
# Create your views here.

def home_page(request, page=1):
    # context_object_name='posts_list'
    # model = Post
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 1)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {
        "post" : page_obj,
        }
    return render (request, 'home.html', context)



# class BlogListView(ListView):
    # queryset  = Post.objects.all()
    # context_object_name='posts_list'
    # paginate_by = 3
    # model = Post
    # template_name = 'home.html'
    
    # def get_queryset(self):
    #     """Return Schools """
    #     return models.Post.objects.order_by('id')
    

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'