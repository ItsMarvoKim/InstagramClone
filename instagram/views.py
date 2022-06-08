from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from .forms import SignUpForm,LoginForm,ProfileForm, ImageForm, CommentForm
from .token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from .models import Profile, Image, Comment, Like
from .email import activation_email
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login')
def home(request):
    images = Image.objects.all()
    return render(request,'home.html', {"images":images})
    
def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            to_email = form.cleaned_data.get('email')
            activation_email(user, current_site, to_email)
            return 'Check your email'
    else:
        form = SignUpForm()
    return render(request, 'django_registration/registration_form.html', {"form":form})


def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request,user)
            return redirect(profile)
        else:
            HttpResponse("Activation link is invalid")
def login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            
            user = authenticate(username,password)
            if user.is_active:
                login(request,user)
                return redirect(home)
            else:
                return HttpResponse("Your account is inactive")
            
    else:
        form=LoginForm()
    return render(request, 'registration/login.html',{"form":form})

def profile(request):
    current_user = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect(home)
    else:
        form = ProfileForm()
    return render(request, 'profile.html',{"form":form})
def profile_user(request, id):
    current_user = request.user
    profile = Profile.objects.filter(user_id=id).all()
    images = Image.objects.filter(profile_id=current_user.profile.id).all()
    return render(request, 'display_profile.html', {"profile":profile, "images":images})

def post_image(request):
    current_user = request.user
    if request.method=='POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user.profile
            image.save()
            return redirect(home)
    else:
        form = ImageForm()
    return render(request, 'post_image.html',{"form":form})

def specific_image(request, img_id):
    image = Image.objects.get(pk=img_id)
    no_of_likes = image.like_set.all().count()
    comments = Comment.objects.filter(image_id=img_id).all()
    return render(request,'single_image.html',{"image":image, "comments":comments, "no_of_likes":no_of_likes})

def search_user(request):
    if 'user' in request.GET and request.GET['user']:
        search_user = request.GET.get('user')
        searched_users = Profile.search_by_profile(search_user)
        message = f'{search_user}'
        return render(request, 'search_profile.html',{"users":searched_users, "message":message})

def write_comment(request, id):
    current_user = request.user
    image = Image.objects.get(pk=id)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id = current_user
            comment.image_id = image
            comment.save_comment()
            return redirect(home)
    else:
        form= CommentForm()
    return render(request, 'write_comment.html', {"form":form, "image":image})
    
def likes(request, img_id):
    current_user = request.user
    current_image = Image.objects.get(pk=img_id)
    new_like= Like.objects.create(user=current_user, image=current_image)
    
    return redirect(home)

def logout_view(request):
    logout(request)
    
    return redirect(home)
        
        
        
    