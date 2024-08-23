from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import BlogModel
from .forms import BlogModelForm

def blog_list(request):
    blogs = BlogModel.objects.all()
    template = loader.get_template("blog_list.html")
    context = {
        "blogs": blogs
    }
    return HttpResponse(template.render(context=context,request=request))


def blog_form(request,id=None):
    if request.method == "GET":
        title = "Add Blog"
        if id is None:
            form = BlogModelForm()
        else:
            blog = BlogModel.objects.get(pk=id)
            form = BlogModelForm(instance=blog)
            title = blog.title
        context={
            "form":form,
            "title":title
        }
        template = loader.get_template("blog_form.html")
        return HttpResponse(template.render(context=context,request=request))
    else:
        if id is None:
            form = BlogModelForm(request.POST)
        else:
            blog = BlogModel.objects.get(pk=id)
            form = BlogModelForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
        return redirect("blog_list")


def blog_delete(request,id):
    blog = BlogModel.objects.get(pk=id)
    blog.delete()
    return redirect("blog_list")