from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('activate/<str:uidb64>/<str:token>/',views.activate, name='activate'),
    path('profile/', views.profile, name='create-profile'),
    path('profile/<int:id>', views.profile_user, name='dipslay-profile'),
    path('post/image/',views.post_image,name='post-image'),
    path('search/', views.search_user, name='search-user'),
    path('comment/<int:id>', views.write_comment, name='write-comment'),
    path('image/<int:img_id>', views.specific_image, name='single-image'),
    path('likes/<int:img_id>', views.likes, name='likes'),
    path('logout/', views.logout_view, name='logout')
    

]


