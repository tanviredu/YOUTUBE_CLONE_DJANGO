from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SignupForm,LoginForm,EditProfile
from .models import Profile


def sign_up(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(data = request.POST)
        if form.is_valid():
            ## save the model and get the user from the form
            user = form.save()
            ## add the user_profile the user
            user_profile = Profile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse("login_app:login"))
            #return HttpResponseRedirect(reverse('login_app:login'))
    return render(request,'login_app/signup.html',{'form':form})

def login_page(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user     = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                #return HttpResponse("You are logged in")
                return HttpResponseRedirect(reverse('stream_app:home'))
    
    return render(request,'login_app/login.html',{'form':form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_app:login'))

@login_required
def profile(request):
    return render(request,'login_app/profile.html',{})

@login_required
def edit_profile(request):
    ## fetch the current users profile objects
    current_user_profile = Profile.objects.get(user=request.user)
    form = EditProfile(instance=current_user_profile)
    if request.method == "POST":
        form = EditProfile(request.POST,request.FILES,instance=current_user_profile)
        if form.is_valid():
            form.save()
            ## reset the form
            form = EditProfile(instance=current_user_profile)
            return HttpResponseRedirect(reverse('stream_app:home'))
    return render(request,'login_app/edit_profile.html',{'form':form})
            
