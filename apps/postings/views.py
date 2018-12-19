from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, User


def post_page(request):
    if not "id" in request.session:
        return redirect("/")
    context={
        "Post" : Post.objects.all().order_by("-created_at"),
    }
    return render(request, "postings/post_page.html", context)

def allposts(request, user_name):
    if not "id" in request.session:
        return redirect("/")
    context ={
        "postes" : Post.objects.filter(user_name=user_name)
    }
    x = user_name
    return render(request, "postings/all_posts.html", context, x)

def process(request, id):
    errors = Post.objects.post_validator(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/posts/page")
    if request.method == "POST":
        x = User.objects.get(id=id)
        Post.objects.create(user= x, author_name= request.POST["author"],user_name=x.first_name, message=request.POST["quotes"])
    return redirect("/posts/page")

def delete(request, id):
    comment_to_delete = Post.objects.get(id=id)
    comment_to_delete.delete()
    return redirect("/posts/page")


