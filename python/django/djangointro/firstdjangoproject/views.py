from django.shortcuts import render
def index(request):
    return render(request,"index.html")
        
def create_user(request):
    print("Got Post Info....................")
    print(request.POST)
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form,
        "location": location,
        "language" : language,
        "comment" : comment
    }
    return render(request,"show.html",context)