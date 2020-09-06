from django.urls import path

from users.views import Profile, Request

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('request/', Request, name='request')

]