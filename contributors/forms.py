from django import forms
from .models import CreateContributor


ROLE_CHOICES = (
    ('as a developer', 'as a developer'),
    ('as a designer', 'as a designer'),
    ('as a documentation team', 'as a documentation team'),
)


class ContributeModelForm(forms.ModelForm):
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = CreateContributor
        fields = ['name', 'email', 'phone', 'role', 'resume']


