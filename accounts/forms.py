from django.contrib.auth import get_user_model
from django import forms


class MyUserCreationForm(forms.ModelForm):

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['avatar', 'username', 'email', 'first_name', 'password']
