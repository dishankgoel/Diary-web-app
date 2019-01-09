from django import forms
from .models import diary_page
from .models import todo

class diary_page_form(forms.ModelForm):

    class Meta:
        model = diary_page
        fields = ('title', 'text')