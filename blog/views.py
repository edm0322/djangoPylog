from django.shortcuts import render, redirect
from blog.models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()

    context = {
        "posts" : posts,
    }

    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    print(post)

    context = {
        "post" : post
    }
    return render(request, "post_detail.html", context)

def post_add(request):
    if request.method == "POST":
        print("Method POST")
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(
            title=title,
            content=content,
        )
        return redirect(f"/posts/{post.id}/") #작성 후 작성된 페이지로 Redirction
    else:
        print("method GET")
    return render(request, "post_add.html")