from django.shortcuts import render, redirect
from accounts.forms import MyUserCreationForm, Login
from django.contrib import auth
from django.http import HttpResponseRedirect
# Create your views here.


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("market")


def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("core/market.html{")
            return render(request,  'core/market.html')
    else:
        form = MyUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def password_reset_form(request):
    return render(request, 'registration/password_reset_form.html')


def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')


def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html')


def password_reset_confirm(request):
    return render(request, 'registration/password_reset_confirm.html')
