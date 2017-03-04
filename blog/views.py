from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm, PostPhotoDirectForm, PhotoUnsignedDirectForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

from django.http import HttpResponse, HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

from cloudinary.forms import cl_init_js_callbacks
from cloudinary import api # Only required for creating upload presets on the fly




def post_list(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html',{'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html', {'post': post})


def post_new(request):
    #direct_form = PostPhotoDirectForm()
    context = dict(
        backend_form = PostForm(),
        #direct_form = direct_form,
        )
    #cl_init_js_callbacks(context['direct_form'], request)
    if request.method=="POST":
        #only backend upload should be here
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) 
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_new.html',context)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'blog/post_edit.html',{'form': form } )

#def post_new(request):
    #context = dict(direct_form = PostPhotoDirectForm())
    #cl_init_js_callbacks(context['direct_form'], request)
    #return render(request, 'post_new.html', context)


def post_draft_list(request):
    posts=Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts':posts})


def post_publish(request, pk):
    post=get_object_or_404(Post, pk=pk)
    
    post.published_date = timezone.now()
    post.save()
    return redirect('post_detail', pk=post.pk)

@csrf_exempt
def direct_upload_complete(request):
    form = PostPhotoDirectForm(request.POST)
    if form.is_valid():
        post=form.save(commit=False)
        post.author=request.user
        post.save()
        # Create a model instance for uploaded image using the provided data
        
        ret = dict(photo_id = post.instance.id)
    else:
        ret = dict(errors = form.errors)

    return HttpResponse(json.dumps(ret), content_type='application/json')

def upload_prompt(request):
    context = dict(direct_form = PostPhotoDirectForm())
    cl_init_js_callbacks(context['direct_form'], request)
    return render(request, 'blog/post_new.html', context)

def post_new_image(request):
    form = PostPhotoDirectForm(request.POST)
    cl_init_js_callbacks(form, request)
    if request.method=='POST':
        form = PostPhotoDirectForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.image=form.cleaned_data['image']
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostPhotoDirectForm()
    return render(request, "blog/post_new_image.html", {'form':form})



