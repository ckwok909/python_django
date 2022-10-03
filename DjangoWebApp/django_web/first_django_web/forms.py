from django import forms
from django.core import validators
from first_django_web.models import PeopleRecord


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']

        if email != v_email:
            raise forms.ValidationError("Make sure emails match")


class NewUserForm(forms.ModelForm):
    class Meta:
        model = PeopleRecord
        fields = '__all__'
