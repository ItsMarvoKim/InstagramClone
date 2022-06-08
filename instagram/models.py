from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
class Profile(models.Model):
    profile_photo = CloudinaryField('profile_photo')
    bio = models.TextField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follower_user = models.IntegerField(blank=True , null=True)
    following_user = models.IntegerField(blank=True, null=True)
    
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
    @classmethod
    def get_prof_id(cls, id):
        profile = cls.objects.filter(id=id).all()
        return profile
    def update_profile(self, bio):
        self.bio = bio
        self.save()
    
    @classmethod
    def search_by_profile(cls,search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles
        
        
    
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    image_location = CloudinaryField('image_location')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def get_img_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image
    
    def update_cap(self, image_caption):
        self.image_caption = image_caption
        self.save()
    
class Comment(models.Model):
    comment = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    
    def save_comment(self):
        self.save()
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    
    def save_like(self):
        self.save()

class Followers(models.Model):
    f_user = models.ForeignKey(Profile, related_name='%(class)s_follower_user',on_delete=models.CASCADE)
    following_u = models.ForeignKey(Profile,related_name='%(class)s_following_user',on_delete=models.CASCADE)
    
        
    
    
