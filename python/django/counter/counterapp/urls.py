from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index, name='index-url'),
    path('destroy_session', views.destroy_session)
]