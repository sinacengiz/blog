from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
from django.contrib.auth.decorators import login_required
def articles(request):
    articles=Article.objects.all()
    return render(request,"articles.html",{"articles":articles})
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashboard(request):
    articles=Article.objects.filter(author=request.user)#bu sayede sisteme 
    #kim giriş yapmıssa onun article larını alıorum
    context={
        "articles":articles
    } #context imi boylelikle return e gönderirim
    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
def addarticle(request):
    form=ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)# mdelden olustugu icin form boyle save edebildim
        article.author=request.user
        article.save()
        messages.info(request,"kaydoldu...")
        return redirect("index")

    return render(request,"addarticle.html",{"form":form})
def detail(request,id):
    #article=Article.objects.filter(id=id).first()
    article=get_object_or_404(Article,id=id)
    return render(request,"detail.html",{"article":article})
@login_required(login_url="user:login")
def deleteArticle(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"silindi...")
    return redirect("article:dashboard")
@login_required(login_url="user:login")
def updateArticle(request,id):
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"güncellendi...")
        return redirect("index")
    return render(request,"update.html",{"form":form})