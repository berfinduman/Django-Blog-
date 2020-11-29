from django.shortcuts import render, HttpResponse,redirect,get_object_or_404 , reverse
from .models import Article, Comment
from .forms import Addarticle
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def articles(request):
    keyword=request.GET.get("keyword")
    if keyword:
        articles=Article.objects.filter(title__contains = keyword)
        return render(request, "articles.html", {"articles": articles})





    articles=Article.objects.all()
    return render(request, "articles.html", {"articles": articles})





def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def article(request,id):
    #article=Article.objects.filter(id=id)
    article=get_object_or_404(Article, id=id)

    comments=article.comments.all()

    
    return render(request, "article.html",{"article":article,"comments":comments})
@login_required(login_url="user:login")
def dashboard(request):
    articles= Article.objects.filter(author=request.user)
    context={"articles": articles}
    return render(request,"dashboard.html",context)
   
@login_required(login_url="user:login")
def addArticle(request):
    form= Addarticle(request.POST or None, request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Makaleniz başarıyla yüklendi.")
        return redirect("dashboard")

    context={"form": form}
    return render(request, "addarticle.html",context)

@login_required(login_url="user:login")
def updateArticle(request, id):
    article=get_object_or_404(Article, id=id)
    form=Addarticle(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Makaleniz başarıyla güncellendi.")
        return redirect("dashboard")
    return render(request, "update.html", {"form": form})

@login_required(login_url="user:login")
def deleteArticle(request, id):
    article=get_object_or_404(Article, id=id)
    
    article.delete()

    messages.warning(request,"Makale silindi.")
    return redirect("dashboard")

def addComment(request, id):
    article= get_object_or_404(Article, id=id)
    if request.method=="POST":
        comment_author= request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
        newComment=Comment(comment_author=comment_author, comment_content=comment_content)
        newComment.article=article
        newComment.save()
    return redirect(reverse("article:article", kwargs={"id": id}))


