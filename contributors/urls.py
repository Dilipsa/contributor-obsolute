from django.views import generic

from django.urls import path
from .views import (
            create_contributor_view,
            #contributor_list_view,
            ContributorListView,
            home_view,
        )

app_name = 'contributors'
urlpatterns = [
    path('', home_view, name='home'),
    path('thank-you', generic.TemplateView.as_view(template_name='contributors/thank_you.html'), name='thank_you'),
    path('create-contributor', create_contributor_view, name='create_contributor'),
    path('contributor-list', ContributorListView.as_view(), name='contributor_list'),
    #path('contributor-list', contributor_list_view, name='contributor_list'),
]