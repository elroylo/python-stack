from django.urls import path

from . import views

urlpatterns = [
    # Rendering Routes
    path('', views.index),
    #path('quotes', views.view_all_quotes),
    #path('users/<int:user_id>', views.view_user),
    #path('quotes/<int:quote_id>', views.view_quote),
    #path('quotes/add', views.view_add_quote_form),
    #path('quotes/<int:quote_id>/like/', views.like_quote),

    # Processing Route
    path('logout', views.logout_session),
    path('register', views.register),
    path('login', views.login_user),
    path('jobs', views.view_all_jobs),
    path('jobs/add', views.add_job),
    path('jobs/edit/<int:job_id>', views.edit_job),
    path('jobs/remove/<int:job_id>', views.remove_job),
    path('jobs/view/<int:job_id>', views.view_job)

]