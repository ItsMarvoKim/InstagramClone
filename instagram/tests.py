from django.test import TestCase
from .models import Profile, Image, Comment, Followers, Like
from django.contrib.auth.models import User

class ImageModelTestClass(TestCase):
    def setUp(self):
    
        self.user_sam = User(username='arondasamuel123', email='arondasamuel123@gmail.com', password='123456')
        self.profile_one = Profile(profile_photo='/path/image.png', bio='This is my bio', user=self.user_sam)
        self.image_one = Image(image_name='Football', image_caption='This football',image_location='/path/image.png', profile=self.profile_one)
        
        
    def test_save_image(self):
        self.user_sam.save()
        self.profile_one.save()
        self.image_one.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)
        
    def test_delete_image(self):
        self.user_sam.save()
        self.profile_one.save()
        self.image_one.save_image()
        self.image_one.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)
        
    def test_update_caption(self):
        self.user_sam.save()
        self.profile_one.save()
        self.image_one.save_image()
        self.image_one.get_img_id(self.image_one.id)
        self.image_one.update_cap('This is not Football')
        self.assertTrue(self.image_one.image_caption=='This is not Football')
        
class ProfileModelTestClass(TestCase):
    def setUp(self):
        self.user_john = User(username='johndoe', email='johndoe@gmail.com', password='abcdef')
        self.profile_two = Profile(profile_photo='/path/imgtwo.png', bio='This is the second bio', user=self.user_john)
        
        
    def test_save_profile(self):
        self.user_john.save()
        self.profile_two.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    def test_delete_profile(self):
        self.user_john.save()
        self.profile_two.save_profile()
        self.profile_two.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)== 0)
        
    def test_update_bio(self):
        self.user_john.save()
        self.profile_two.save_profile()
        self.profile_two.get_prof_id(self.profile_two.id)
        self.profile_two.update_profile('This is the third bio')
        self.assertTrue(self.profile_two.bio=='This is the third bio')
    
    def test_search_by_profile(self):
        self.user_john.save()
        self.profile_two.save_profile()
        profiles = self.profile_two.search_by_profile('johndoe')
        
        self.assertTrue(len(profiles) > 0)

class CommentTestClass(TestCase):
    def setUp(self):
        self.user_jack = User(username='jack', email='jackdoe@gmail.com', password='abcdef')
        self.profile = Profile(profile_photo='/path/imgthree.png', bio='I am Jack', user=self.user_jack)
        self.image_three = Image(image_name='Food', image_caption='Juicy steak',image_location='/path/imgfour.png', profile=self.profile)
        self.comment_one = Comment(comment='This food looks delicious', user_id=self.user_jack, image_id=self.image_three)
        
        
    
    def test_save_comments(self):
        self.user_jack.save()
        self.profile.save_profile()
        self.image_three.save_image()
        self.comment_one.save_comment()
        comments = Comment.objects.all()
        
        self.assertTrue(len(comments)> 0)
        
class LikeModelTestClass(TestCase):
    def setUp(self):
         self.user_jane = User(username='jane', email='janedoe@gmail.com', password='abcdef12')
         self.profile = Profile(profile_photo='/path/imgfour.png', bio='I am Jack', user=self.user_jane)
         self.image_four = Image(image_name='Food', image_caption='Juicy steak',image_location='/path/imgfive.png', profile=self.profile)
         self.like_photo = Like(likes=20, user_id=self.user_jane, image_id=self.image_four)
         
         
    def test_save_likes(self):
        self.user_jane.save()
        self.profile.save_profile()
        self.image_four.save_image()
        self.like_photo.save_like()
        likes = Like.objects.all()
        self.assertTrue(len(likes)> 0)
        
        

        
        
        
        
        