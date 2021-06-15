from django.shortcuts import render, redirect
from random import randint
# Create your views here.
def index(request):
    return render(request, context={'gold':request.session.get('gold', 0), 'activities':request.session.get('activities', [])}, template_name='index.html')

def process_money(request):
    money = 0
    activities = []
    if 'gold' in request.session:
        money = request.session['gold']
    else:
        request.session['gold'] = 0

    if 'activities' in request.session:
        activities = request.session['activities']
    else:
        request.session['activities'] = []
    # add money
    if request.POST.get('place') == "Farm":
        x = randint(10,20)
        money += x
        activities.append('You went to the farm and made ' + str(x) + ' gold')

    if request.POST.get('place') == "Cave":
        x = randint(5,10)
        money += x
        activities.append('You went to the Cave and made ' + str(x)+ ' gold')

    if request.POST.get('place') == "House":
        x = randint(2,5)
        money += x
        activities.append('You went to the House and made ' + str(x)+ ' gold')

    if request.POST.get('place') == "Casino":
        x = randint(-50,50)
        money += x
        if x >= 0:
            activities.append('You went to the Casino and made ' + str(x)+ ' gold') 
        else:
            activities.append('You went to the Casino and lost' + str(x)+ ' gold')   

    # save money
    request.session['gold'] = money
    request.session['activities'] = activities
    return redirect(to='index-url')

def destroy_session(request):
    request.session.clear()
    return redirect(to='index-url')