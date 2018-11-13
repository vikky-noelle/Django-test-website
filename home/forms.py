from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class subsform(forms.Form):
    your_email = forms.EmailField(label='Email', max_length=100)
