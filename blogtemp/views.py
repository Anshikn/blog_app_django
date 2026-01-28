from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
# Create your views here.

def blog_index(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
            
        Blog.objects.create(
            title=title,
            body=body
            )    
    blogs = Blog.objects.all()
    context = {
         'blogs': blogs,
    }
    return render(request, 'blogtemp/index.html', context)


# def get_blogs(request):
#     blogs = Blog.objects.all()
#     return render(request, 'blogtemp/index.html', {'blogs': blogs})
# def add_blog(request):
 
def delete_blog(request, blog_id):
    # blog = Blog.objects.get(id=blog_id)
    blog = get_object_or_404(Blog, id = blog_id)
    blog.delete()
    return redirect('blog_index')

def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id = blog_id)
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.body = request.POST.get('body')
        blog.save()
        return redirect('blog_index')
    
