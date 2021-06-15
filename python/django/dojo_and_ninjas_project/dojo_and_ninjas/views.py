from django.shortcuts import render, redirect
from .models import Dojo, Ninja
# Create your views here.
def index(request):
    context = {
        "all_the_dojos": Dojo.objects.all(),
        "all_the_ninjas": Ninja.objects.all()
    }
    return render(request, "index.html", context)

def create_dojo(request):
    print("Got Post Info....................")
    print(request.POST)
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    Dojo.objects.create(name = name, city = city, state = state)
    return redirect(to='index-url')


def create_ninja(request):
    print("Got Post Info....................")
    print(request.POST)
    dojo_id = request.POST['dojo_id']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    Ninja.objects.create(dojo_id = dojo_id, first_name = first_name, last_name = last_name)
    return redirect(to='index-url')
