from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm


def signup_view(request):
    form=CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Created Successfully for ' + user)
            return redirect('login')


    context={'form':form}
    return render(request, 'signup.html', context)
