from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
# Create your views here.
from .models import Assign, Project
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from .forms import RegistrationForm, SubmitProjectTopic




def index(request):
    return render(request, 'student/student.html')



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)
            return redirect('student:dashboard')
        else:
            return render(request, 'student/login.html', {'login_form':form})
    else:
        form = AuthenticationForm()
    return render(request, 'student/login.html', {'login_form':form})


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            user = form.save()
            created = True
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            context = {'created' : created}
            return render(request, 'student/register.html', context)
        else:
            return render(request, 'student/register.html', context)
    else:
        form = RegistrationForm()
        context = {
            'form' : form,
        }
        return render(request, 'student/register.html', context)




def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('student:login'))



def dashboard(request):
    return render(request, 'student/landing.html')




def newProject(request):
    if request.method == 'POST':
        form = SubmitProjectTopic(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = SubmitProjectTopic()
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'student/new_project.html', context)
        else:
            return render(request, 'student/new_project.html', context)
    else:
        form = SubmitProjectTopic()
        context = {
            'form': form,
        }
        return render(request,'student/new_project.html', context)





def usersView(request):
    # users = UserProfile.objects.all()
    # tasks = Task.objects.all()

    allcontent = Assign.objects.all()
    
    context = {
        # 'users': users,
        # 'tasks': tasks,
        'allcontent': allcontent
    }
    return render(request, 'student/supervisor.html', context)





def list(request):

   
    topic_no = "Topic No:"
    projectList = Project.objects.get(id=profile_id)
    
    context = {
        
        'ProjectList': projectList,
        'TopicNo' : topic_no
    }
    return render(request, 'student/projectList.html', context)