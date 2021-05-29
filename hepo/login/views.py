from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render


from django.contrib.auth import authenticate, login, logout

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('chatmenu')
        else:
            messages.info(request, 'username OR password is incorrect')

    return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    return redirect('login')
