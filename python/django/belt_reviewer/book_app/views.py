from django.contrib import messages
from django.shortcuts import redirect, render

import bcrypt

from .models import *

# Create your views here.

# Render Templates

def index(request):
    return render(request, 'index.html')


def view_all_quotes(request):
    # if we don't have a user in session
    if 'user_id' not in request.session:
        # redirect them
        return redirect('/')
    context = {
        'all_reviews': Review.objects.all().order_by('created_at')[0:3],
        'all_quotes': Quote.objects.all()
    }
    return render(request, 'quotes.html', context)


def view_user(request, user_id):
    # if we don't have a user in session
    if 'user_id' not in request.session:
        # redirect them
        return redirect('/')
    print(user_id)
    context = {
        'entire_logged_in_user_object': User.objects.get(id=user_id)
    }
    return render(request, 'user.html', context)


def view_quote(request, quote_id):
    # if we don't have a user in session
    if 'user_id' not in request.session:
        # redirect them
        return redirect('/')
    print(quote_id)
    context = {
        'quote': Quote.objects.get(id=quote_id)
    }
    return render(request, 'quote.html', context)


def view_add_quote_form(request):
    # if we don't have a user in session
    if 'user_id' not in request.session:
        # redirect them
        return redirect('/')
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'add_quote.html', context)


# Redirect routes

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
        return redirect('/quotes')


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
        return redirect('/quotes')


def create_a_quote(request):
    print(request.POST)
    # create a quote
    newly_created_quote = Quote.objects.create(
        quote_title=request.POST['quote_title'],
        quote_desc = request.POST['quote_desc']
    )

    # check if we need a new author
    if request.POST['new_author'] != '':
        print('we need a new author')
        # create a new author
        new_author = Author.objects.create(
            full_name=request.POST['new_author'])
        # associate it with the book
        newly_created_quote.authors.add(new_author)
        # we only need to add it one way
        # new_author.all_books.add(newly_created_book)
    else:
        # use existing author
        print('we will use an existing author')
        # get existing author instance from db
        matching_author = Author.objects.get(
            id=request.POST['existing_author_id'])
        newly_created_quote.authors.add(matching_author)

    # always
    # create a review
    Review.objects.create(
        text=request.POST['quote_text'],
        user_who_wrote_this=User.objects.get(id=request.session['user_id']),
        quote=newly_created_quote
    )

    return redirect('/quotes/' + str(newly_created_quote.id))


def create_review(request):
    print(request.POST)
    # create a review
    Review.objects.create(
        text=request.POST['quote_text'],
        user_who_wrote_this=User.objects.get(id=request.session['user_id']),
        quote=Quote.objects.get(id=request.POST['quote_id'])
    )
    return redirect('/quotes/' + request.POST['quote_id'])


def quote_remove(request, quote_id):
    to_delete = Quote.objects.get(id=quote_id)
    to_delete.delete()
    return redirect('/quotes')

def like_quote(request, quote_id):
    current_user_id = request.session['user_id']
    #id = request.user.id
    current_user = User.objects.get(id=current_user_id)
    current_quote = Quote.objects.get(id=quote_id)
    current_quote.users_likes.add(current_user)
    current_quote.save()
    return redirect('/quotes')

def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('update_profile_success'))
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'registration/update_profile.html', args)