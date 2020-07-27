from django.shortcuts import render, HttpResponse, redirect
from .models import Blog, Comments
from  .forms import CommentsForm
# Create your views here.

def show_all_blog(request):
    blogs = Blog.objects.all()  #.order_by("priority")
    print(blogs)

    context = {
        "blog_list": blogs
    }

    return render(request, "blogs.html", context)


def show_blog(request, slug_text):
    blog = Blog.objects.filter(slug=slug_text)
    if blog.exists():
        blog = blog.first()
        comments = Comments.objects.filter(blog=blog)
        print(comments)
    else:
        return HttpResponse("<h1>Page Not Found</h1>")
    print("debug 1", blog)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.blog = blog
            user.save()
            print(user)
            return redirect(f"/blog/{slug_text}")
        else:
            print(form.errors)
            # return redirect(f"/blog/{slug_text}")


    else:
        form = CommentsForm()
    
    context = {
        "blog": blog,
        "form": form,
        "comments": comments
    }
    return render(request, "single-blog.html", context)