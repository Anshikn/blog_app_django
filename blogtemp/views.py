from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def blog_index(request):
    # user_id = request.user.id
    
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        body = request.POST.get('body', '').strip()
        user = request.user

        if title and body:   
            Blog.objects.create(
                title=title,
                body=body,
                user = user
                )    
            return redirect('blog_index')
        
    blogs = Blog.objects.all().order_by('-id')
    context = {
         'blogs': blogs,
    }
    return render(request, 'blogtemp/index.html', context)


# def get_blogs(request):
#     blogs = Blog.objects.all()
#     return render(request, 'blogtemp/index.html', {'blogs': blogs})
# def add_blog(request):
 
@login_required
def delete_blog(request, blog_id):
    # blog = Blog.objects.get(id=blog_id)
    blog = get_object_or_404(Blog, id = blog_id)
    if blog.user != request.user:
        return HttpResponseForbidden()
    else:
        blog.delete()
    return redirect('blog_index')

@login_required
def edit_blog(request, blog_id):

    blog = get_object_or_404(Blog, id = blog_id)
    # user = request.user
    if blog.user != request.user:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        body = request.POST.get('body', '').strip()

        if title and body:
            blog.title = request.POST.get('title')
            blog.body = request.POST.get('body')
            blog.save()
            return redirect('blog_index')
        
    return render(request, 'blogtemp/edit.html', {'blog': blog})
        

