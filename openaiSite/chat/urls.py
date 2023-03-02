
from django.urls import path

from . import views

urlpatterns =[
    path("say",views.chat,name='chat'),
    path("image",views.image,name='image'),
    path("edit",views.edit,name='edit'),
    path("test",views.test,name='test'),
    path("index",views.test,name='index'),
]