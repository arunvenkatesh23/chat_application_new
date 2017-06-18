from django.conf.urls import url
from . import views

app_name = "chat_room"

urlpatterns = [
    url(r'^home/$', views.index, name='index'),

    url(r'^post/$', views.post, name='post'),
    url(r'^messages/$', views.messages, name='messages'),
    url(r'profile_settings/$', views.profile_settings, name='profile'),
]
