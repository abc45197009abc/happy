from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
import random
# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
    
def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        return render(request, 'post.html', {'post': post})
    except Post.DoesNotExist:
        return redirect("/")  # 書本不存在，重定向到首頁   
def about(request,num=-1):
    quotes = ['今日事，今日畢',
            '要怎麼收穫，先那麼栽',
            '知識就是力量',
            '一個人的個性就是他的命運']    
    if num ==-1 or num>4:
        quote = random.choice(quotes)
    else:
        quote = quotes[num]
    return render(request, 'about.html', locals()) 

'''
    post = Post.objects.get(slug=slug) 
    return render(request, 'post.html', locals())
    #select * from post where slug=%slug

def homepage(request):
    posts = Post.objects.all() #select * from post
    post_lists = list()
    for counter, post in enumerate(posts):
        post_lists.append(f'No. {counter}-{post} <br>')
    return HttpResponse(post_lists)
'''