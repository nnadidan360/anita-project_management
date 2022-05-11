from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from .forms import RegistrationForm, SubmitProjectTopic


def login_admin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)
            # return redirect('student:dashboard')
        else:
            return render(request, 'login.html', {'login_form':form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'login_form':form})
