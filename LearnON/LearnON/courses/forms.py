from django import forms
from django.contrib.auth.models import User
from .models import Class, Subjects, Lesson



class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'
        help_texts = {
            'title': 'For example. Class 11 or Class of Informatics',
            'description':'Put a short description of the class',
            'image':'You can put a picture of the class or it can be left blank'
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['creator','slug', 'title', 'classs', 'description', 'image_case']
        help_texts = {
            'title': 'For example. Mathematics, Geography etc.',
            'description':'Put a brief description of the subject',
            'classs':'Choose the class for which you will create the subject',
            'image_case':'You can put a photo of the subject or it can be left blank'
        }
        labels = {
            'title':'Title of the subject',
            'classs':'Class',
            'image_case':'Image',
        }
        widgets = {'creator': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class TeachingForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','title', 'case', 'video_id', 'position', ]
        help_texts = {
            'title':'Enter the title of the lesson',
            'case':'Choose the subject for which this lesson belongs',
            'video_id':'Enter the Youtube video ID you will upload (<a href="/media/youtube_help.png"> where can i find the ID </a>)',
            'position':'Enter the lesson number'
        }
        labels={
            'case':'Subject',
            'position':'Lesson No.',
        }
        widgets = {
            'slug': forms.HiddenInput()
        }