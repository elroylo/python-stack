from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index, name='index-url'),
    path('process_money', views.process_money, name='process_money-url'),
    path('clear', views.destroy_session, name='clear-url')
]