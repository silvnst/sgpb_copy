from django.contrib.auth import models
from django.forms import fields
from .models import Method
from django import forms
from django.forms import Textarea


class MethodForm(forms.ModelForm):

    class Meta:
        model = Method
        fields = '__all__'