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
from .forms import RegistrationForm
from student.models import Assign




def register_supervisor(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            user = form.save()
            created = True
            is_Staff = True
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            context = {'created' : created}
            return render(request, 'supervisor/register_supervisor.html', context)
        else:
            return render(request, 'supervisor/register_supervisor.html', context)
    else:
        form = RegistrationForm()
        context = {
            'form' : form,
        }
        return render(request, 'supervisor/register_supervisor.html', context)






def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'], )
            # if authenticated_user == is_Staff:
            login(request, authenticated_user)
            # else:
            #     msg = "You have to be a Supervisor to login"
                # return render('supervisor:signin.html', {'msg': msg})
            return redirect('supervisor:dashboard')
        else:
            return render(request, 'supervisor/signin.html', {'login_form':form})
    else:
        form = AuthenticationForm()
    return render(request, 'supervisor/signin.html', {'login_form':form})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('supervisor:login'))


def dashboard(request):
    return render(request, 'supervisor/landing.html')


def usersView(request):
    
    project = Assign.objects.all()

    context = {
        'project': project
    
    }
    return render(request, 'supervisor/project_list.html', context)
