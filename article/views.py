from django.contrib import messages
from article.models import Article, Comment
from django import forms
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render,reverse
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {"articles" :articles,}
    return render(request,"dashboard.html",context)

def article(request,id):
    article = Article.objects.filter(id = id).first()
    comments = article.comments.all()
    context = {"article" : article,"comments":comments}
    return render(request,"article.html",context)

def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles" : articles,})
    articles = Article.objects.all()
    return render(request,"articles.html",{"articles" : articles,})

@login_required(login_url = "user:login")
def addarticle(request):

    form = ArticleForm(request.POST or None,request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makaleniz Başarıyla Oluşturuldu.")
        return redirect("article:dashboard")
        
    return render(request,"addarticle.html",{"form" :form,})

@login_required(login_url = "user:login")
def edit(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makaleniz Başarıyla Güncellendi.")
        return redirect("article:dashboard")

    return render(request,"edit.html",{"form":form})

@login_required(login_url = "user:login")
def delete(request,id):
    deleteArticle = Article.objects.filter(id = id,author = request.user).first()
    if deleteArticle:
        Article.objects.filter(id = id).delete()
        messages.success(request,"Makale başarıyla silindi.")
        return redirect("article:dashboard")
    else:
        messages.info(request,"Böyle bir makale yok veya böyle bir makaleyi silme yetkiniz yok.")
        return redirect("index")


def addComment(request,id):
    article = get_object_or_404(Article,id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author,comment_content=comment_content)
        newComment.article = article
        newComment.save()
        messages.success(request,"Yorumunuz Başarıyla Eklendi")

    return redirect(reverse("article:article",kwargs = {"id":id}))
        


