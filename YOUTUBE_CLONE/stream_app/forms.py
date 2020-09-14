from django import forms
from .models import Video,Comment

class UploadForm(forms.ModelForm):
    class Meta:
        model  = Video
        fields = ['video_title','video_content','thumbnail']

class CommentForm(forms.ModelForm):
    class Meta:
        model  = Comment
        fields = ['comment']  
