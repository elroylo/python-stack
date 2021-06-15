from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index, name='index-url'),
    path('create_user', views.create_user, name='create-user')
]