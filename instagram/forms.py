from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile,Image,Comment

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',max_length=254)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        exlcude = ['follower_user', 'following_user']
        fields = ('bio', 'profile_photo')
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile']
        fields = ('image_name', 'image_caption','image_location')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image_id', 'user_id']
        fields = ('comment',)
    
    