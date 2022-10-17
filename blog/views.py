from django.shortcuts import get_object_or_404, render,get_list_or_404
from django.http import HttpResponse
import datetime
from django.views.generic import TemplateView
from .models import book,Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import commentform

# Create your views here.

def displayTime(request):
    now = datetime.datetime.now()
    html = "Time is {}" .format(now)
    return HttpResponse(html)

def greet(request):
    html ="Welcome to my page"
    return HttpResponse(html)

class MyView(TemplateView):
    template_name = "index.html"
    # def get_context_data(self,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     template_name = "index.html"
    #     context={
    #         'page': template_name
    #     }
    #     return context



def Book_list(request):
        books= book.objects.all()
        return render(request,"index.html",{"books": books})

def book_details(request, id):
        context = {
            "detail": get_object_or_404(book, pk=id)
        }
        return render(request,"details.html",context)

def post_list(request):
    object_list =Post.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,"index.html",{"posts":posts})

#view for single post
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',publish__year=year, publish__month=month, publish__day= day)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method =='POST':
        comment_form =commentform(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post= post
            new_comment.save() 
    else:
        comment_form= commentform()
    return render(request, 'post_detail.html',{"post":post,"comments":comments,"comment_form":comment_form})