from django.urls import path
from .views import register_view, home_view, signIn_view, header_view 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home_view, name='home'), 
    path('register/', register_view , name='register'), 
    # path('profile/', profile_view  , name="profile"),
    path('signIn/', signIn_view, name='signIn'), 
    path('header/', header_view, name='header'), 
    path('logout/', LogoutView.as_view(next_page='signIn'), name = 'logout'),
  
    
]



