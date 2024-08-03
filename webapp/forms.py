from django import forms
from webapp.models import Topics


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['name', 'content']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=150, required=False, label='Search')
