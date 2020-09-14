from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import UploadForm,CommentForm
from .models import Video,Comment
import uuid


@login_required
def home(request):
    videos = Video.objects.all()
    if request.method == "GET":
        search  = request.GET.get('search','')
        print(search)
        results = Video.objects.filter(video_title__icontains=search)
        print(results)
    return render(request,'stream_app/home.html',{'videos':videos,'search':search,'results':results})


@login_required
def details(request,slug):
    video = Video.objects.get(slug=slug)
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user  = request.user
            comment.video = video
            comment.save()
            return HttpResponseRedirect(reverse('stream_app:video_details',kwargs={'slug':slug}))
    
    return render(request,'stream_app/video_details.html',{'video':video,'form':comment_form})

@login_required
def upload_video(request):
    form = UploadForm()
    if request.method == "POST":
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.slug = str(uuid.uuid4())
            video.save()
            return HttpResponseRedirect(reverse('stream_app:home'))
    return render(request,'stream_app/upload_video.html',{'form':form})


@login_required
def edit_video(request,slug):
    video = Video.objects.get(slug=slug)
    form = UploadForm(instance=video)
    if request.method == "POST":
        form = UploadForm(request.POST,request.FILES,instance=video)
        if form.is_valid():
            form.save()
            form = UploadForm(instance=video)
            return HttpResponseRedirect(reverse('login_app:profile'))
    return render(request,'stream_app/upload_video.html',{'form':form})