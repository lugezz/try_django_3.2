from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        #print (username, password)

        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {'error': 'Invalid user or password'}
            return render(request, 'accounts/login.html', context)

        login (request, user)
        return redirect ('/')
    context = {
    }

    return render(request, 'accounts/login.html', context)
    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect ("/accounts/login")

    return render(request, 'accounts/logout.html', {})
    
def register_view(request):
    
    context = {
    }

    return render(request, 'accounts/register.html', context)