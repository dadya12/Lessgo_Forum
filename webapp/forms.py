from django import forms
from webapp.models import Topics, Answers


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['name', 'content']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ['text']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=150, required=False, label='Search')
