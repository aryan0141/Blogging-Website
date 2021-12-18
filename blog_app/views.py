from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Blog
import datetime
from django.contrib.auth import get_user_model

def index(request):
    user = request.user
    registered_users = len(get_user_model().objects.all()) + 10

    blogs = Blog.objects.all()
    total_blogs = len(blogs) + 20

    money_rewarded = 4000
    for item in blogs:
        money_rewarded+=item.amount_to_pay

    websiteStats = {
        "registered_users": registered_users,
        "total_blogs": total_blogs,
        "money_rewarded": money_rewarded,
    }

    return render(request, "index.html", {'websiteStats' : websiteStats})

def user_dashboard(request, uname):
    user = request.user
    if user.is_authenticated:
        if user.username == uname:
            if request.method == "POST":
                article_name = request.POST["article_name"]
                article_link = request.POST["article_link"]
                blog = Blog(user=user, article_name=article_name, google_doc_link=article_link, date_created = datetime.datetime.now(), updated_by = user.username )
                blog.save()
                messages.info(request,"Blog Succesfully Added")
                return redirect("/profile/" + user.username)
            else:
                shortlistedArticles = 0
                moneyEarned = 0
                pendingArticles = 0
                blogs = Blog.objects.filter(user=user)
                for item in blogs:
                    if item.blog_status == "Shortlisted":
                        shortlistedArticles+=1
                    if item.blog_status == "Pending for review":
                        pendingArticles+=1
                    moneyEarned+=item.amount_to_pay
                userStats = {
                    "shortlistedArticles": shortlistedArticles,
                    "pendingArticles": pendingArticles,
                    "moneyEarned": moneyEarned,
                }
                print(blogs)
                return render(request, "user_dashboard.html", {'blogs' : blogs, 'userStats' : userStats})
        else:
            messages.info(request,"You cannot see other's Dashboard!")
            return redirect("/")
    
    messages.info(request,"Login first to see your Dashboard!")
    return redirect("/")

def deleteBlog(request):
    if request.method == "POST":
        blog_id = request.POST.get("content")
        blog = Blog.objects.get(blog_id=blog_id)
        if blog.blog_status != "Shortlisted":
            blog.delete()
            return HttpResponse("Deleted")
    return HttpResponse("Failed")

def submitForReviewBlog(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            blog_id = request.POST.get("content")
            blog = Blog.objects.filter(blog_id=blog_id).first()

            # This condition os to check that the right person is making the request.
            if user.username == blog.user.username:
                blog.blog_status = "Pending for review"
                blog.date_updated = datetime.datetime.now()
                blog.updated_by = user.username
                blog.save()
                return HttpResponse("Submitted")

    return HttpResponse("Failed")

def editBlog(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            data = request.POST.getlist('data[]')
            blog_id = data[0]
            articleName = data[1]
            articleLink = data[2]
            blog = Blog.objects.filter(blog_id=blog_id).first()

            # # This condition os to check that the right person is making the request.
            if user.username == blog.user.username:
                blog.date_updated = datetime.datetime.now()
                blog.updated_by = user.username
                blog.article_name = articleName
                blog.google_doc_link = articleLink
                blog.save()
                return HttpResponse("Updated")

    return HttpResponse("Failed")

def contact(request):
    return render(request, "contact.html")


