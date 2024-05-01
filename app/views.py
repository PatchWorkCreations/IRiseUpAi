from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')


def blog_2(request):
    return render(request, 'blog-2-col.html')


def blog_3(request):
    return render(request, 'blog-3-col.html')


def blog_full(request):
    return render(request, 'blog-full.html')


def donate(request):
    return render(request, 'donate.html')


def index_03(request):
    return render(request, 'index-03.html')


def single_blog(request):
    return render(request, 'single-blog.html')


def single_left_sidebar(request):
    return render(request, 'single-left-sidebar.html')


def single_right_sidebar(request):
    return render(request, 'single-left-sidebar.html')


def demosample(request):
    return render(request, 'demosample.html')


def popup(request):
    return render(request, 'popup.html')
