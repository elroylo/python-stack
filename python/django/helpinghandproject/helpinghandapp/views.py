from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect, render

import bcrypt

from .models import *

# Create your views here.

# Render Templates

def index(request):
    return render(request, 'index.html')

def view_all_jobs(request):
    # if we don't have a user in session
    if 'user_id' not in request.session:
        # redirect them
        return redirect('/')
    context = {
        'job': Job.objects.all().order_by('created_at')[0:10],
        'entire_logged_in_user_object': User.objects.get(id=request.session['user_id'])

    }
    return render(request, 'jobs.html', context)

def view_job(request, job_id):
    # if we don't have a user in session
    if 'user_id' not in request.session:
        # redirect them
        return redirect('/')
    print(job_id)
    context = {
        'job': Job.objects.get(id=job_id)
    }
    return render(request, 'view_job.html', context)

def view_user(request, user_id):
    # if we don't have a user in session
    if 'user_id' not in request.session:
        # redirect them
        return redirect('/')
    print(user_id)
    context = {
        'entire_logged_in_user_object': User.objects.get(id=user_id)
        }
    return render(request, 'view_user.html', context)


def logout_session(request):
    request.session.flush()
    return redirect('/')

def register(request):
    print(request.POST)
    # run validations
    errors = User.objects.register_validator(request.POST)
    print(errors)
    # generate errors
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        print('we made it in the if block so we have errors')
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value, key)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        # hash the password
        print(request.POST['password'])
        hash_browns = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print('hash_browns: ', hash_browns)
        # create a user
        new_user = User.objects.create(
            name=request.POST['name'],
            alias=request.POST['alias'],
            email=request.POST['email'],
            password=hash_browns,
        )
        # start session
        request.session['user_id'] = new_user.id
        request.session['username'] = new_user.alias
        print('*'*50)
        print(new_user.password)
        return redirect('/jobs')


def login_user(request):
    print(request.POST)
    errors = User.objects.login_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:  # check again
        user_with_matching_email = User.objects.filter(
            email=request.POST['login_email']).first()
        request.session['user_id'] = user_with_matching_email.id
        request.session['username'] = user_with_matching_email.alias
        return redirect('/jobs')

def add_job(request):
    print(request.POST)
    errors = {}
    if(request.method == 'POST'):
        # create a job
        
        if len(request.POST['job_title']) < 3:
            errors["job_title"] = "Job Title should be at least 3 characters."
        if len(request.POST['job_desc']) < 3:
            errors["job_desc"] = "Job Description should be at least 3 characters."
        if len(request.POST['job_location']) < 3:
            errors["job_location"] = "Location should be at least 3 characters."
        if errors == {}:
            newly_created_job = Job.objects.create(
                job_title=request.POST['job_title'],
                user_who_owns_this_id = request.session['user_id'],
                job_desc=request.POST['job_desc'],
                job_location=request.POST['job_location']
                )   
            return redirect('/jobs')    
    context = {
        "errors":errors
    }
    return render(request, 'add_job.html', context)

def edit_job(request, job_id):
    print(request.POST)
    # update job
    if(request.method == 'POST'):
        Job.objects.filter(id=job_id).update(
            job_title=request.POST['job_title'],
            job_desc=request.POST['job_desc'],
            job_location=request.POST['job_location']
        )
        return redirect('/jobs')
    else:
        context = {
            'job':Job.objects.get(id=job_id)
        }
        
        return render(request, 'edit_job.html', context)

def remove_job(request, job_id):
    to_delete =Job.objects.get(id=job_id)
    to_delete.delete()
    return redirect('/jobs')