# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.http import Http404, HttpResponseRedirect

from blog.models import Blog
from blog.forms import CreatBlogForm


def show_blog(request):
    blog_list = Blog.objects.all().order_by('-creat_date')
    rc = RequestContext(request, {
                "blog_list": blog_list,
                })
    return render_to_response('blog/show_blog.html', context_instance=rc)


def blog_id(request, id):
    try:
        b = Blog.objects.get(pk=id)
        form = CreatBlogForm(instance = b)
    except Blog.DoesNotExist:
        raise Http404
    
    if request.method == 'POST': 
        form = CreatBlogForm(request.POST) 
        if form.is_valid(): 
            instance = form.save()
                           
            instance.save()
            return HttpResponseRedirect('/blog/')
            
    rc = RequestContext(request, {
                'blog': b,
                'form':form,
                })
    return render_to_response('blog/blog_id.html', context_instance=rc)
    
def creat_blog(request):
     
    if request.method == 'POST': 
        form = CreatBlogForm(data=request.POST) 
        if form.is_valid(): 
            blog = form.save()
            
            blog.save()
            return HttpResponseRedirect('/blog/') 
    else:
        form = CreatBlogForm(instance=None)
        
    rc = RequestContext(request, {
                "form": form,
                })
    return render_to_response('blog/creat_blog.html', context_instance=rc)
