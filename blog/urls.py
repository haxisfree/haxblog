#blog/urls.py

from django.urls import path
from .views import BlogDetailView, home_page

# app_name = "Blog"
urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', home_page , name='home'),
    path('page/<int:page>', home_page , name='home'),
    # path('page/<int:page>', BlogListView.as_view(), name='home'),
]