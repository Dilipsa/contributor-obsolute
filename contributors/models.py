from django.db import models
from django.shortcuts import reverse

ROLE_CHOICES = (
    ('as a developer', 'as a developer'),
    ('as a designer', 'as a designer'),
    ('as a documentation team', 'as a documentation team'),
)


class CreateContributor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    role = models.CharField(choices=ROLE_CHOICES, max_length=25)
    resume = models.FileField(upload_to='resumes')

    def __str__(self):
        return self.name

    def get_absolute_url(self, *args, **kwargs):
        return reverse('contributors:detail', kwargs={'pk': self.pk})
