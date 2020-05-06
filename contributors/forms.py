from django import forms
from .models import CreateContributor


# ROLE_CHOICES = (
#     ('as a developer', 'as a developer'),
#     ('as a designer', 'as a designer'),
#     ('as a documentation team', 'as a documentation team'),
# )


class ContributeModelForm(forms.ModelForm):

    class Meta:
        model = CreateContributor
        role = forms.CharField

        contributed = forms.BooleanField()
        fields = ['name', 'email', 'phone', 'role', 'resume', 'role']
        widgets = {'contributed': forms.HiddenInput()}
