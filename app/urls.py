from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('blog-2', blog_2, name='blog-2'),
    path('blog-3', blog_3, name='blog-3'),
    path('blog-full', blog_full, name='blog-full'),
    path('donate', donate, name='donate'),
    path('index-03', index_03, name='index-03'),
    path('single-blog', single_blog, name='single-blog'),
    path('single-left-sidebar', single_left_sidebar, name='single-left-sidebar'),
    path('single-right-sidebar', single_right_sidebar, name='single-right-sidebar'),
    path('demosample', demosample, name='demosample'),
    path('popup', popup, name='popup'),
]
