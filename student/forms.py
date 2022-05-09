from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', required=True)

    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        }

        labels = {
            'first_name': 'Name',
            'last_name': 'Last Name',
            'company': 'Company',
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            

        return user

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Retype Password'




class SubmitProjectTopic(forms.ModelForm):
    name = forms.CharField(max_length=30)
    mat_no = forms.CharField(max_length=30)
    topic_1 = forms.CharField(
        widget= forms.Textarea
    )
    topic_2 = forms.CharField(
        widget= forms.Textarea
    )
    topic_3 = forms.CharField(
        widget= forms.Textarea
    )
    
   

    class Meta:
        model = Project
        fields = ('name', 'mat_no', 'topic_1', 'topic_2', 'topic_3')


    def save(self, commit=True):
        project = super(SubmitProjectTopic, self).save(commit=False)
        project.name = self.cleaned_data['name']
        project.mat_no = self.cleaned_data['mat_no']
        project.topic_1 = self.cleaned_data['topic_1']
        project.topic_2 = self.cleaned_data['topic_2']
        project.topic_3 = self.cleaned_data['topic_3']
        
        project.save()
        # assigns = self.cleaned_data['assign']
        # for assign in assigns:
        #     task.assign.add((assign))

        if commit:
            project.save()

        return project
        

        def __init__(self, *args, **kwargs):
            super(SubmitProjectTopic, self).__init__(*args, **kwargs)
            self.fields['name'].widget.attrs['class'] = 'form-control'
            self.fields['name'].widget.attrs['placeholder'] = 'Name'
            self.fields['topic_1'].widget.attrs['class'] = 'form-control'
            self.fields['topic_1'].widget.attrs['placeholder'] = 'Topic 1'
            self.fields['topic_2'].widget.attrs['class'] = 'form-control'
            self.fields['topic_2'].widget.attrs['placeholder'] = 'Topic 2'
            self.fields['topic_3'].widget.attrs['class'] = 'form-control'
            self.fields['topic_3'].widget.attrs['placeholder'] = 'Topic 3'
       