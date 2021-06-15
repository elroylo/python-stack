from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    session = request.session
    if 'counter' in session:
        session['counter'] += 1
        print(session['counter'])
    else:
        print('counter does not exist')
        session['counter'] = 0
    return render(request, context={}, template_name='index.html')

def destroy_session(request):
    del request.session['counter']
    return redirect(to='index-url')
