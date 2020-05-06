from django.shortcuts import render, redirect
from .forms import ContributeModelForm
from .models import CreateContributor
from django.views.generic.list import ListView


def home_view(request):
    return render(request, 'contributors/home.html')


def create_contributor_view(request):
    if request.method == "POST":
        form = ContributeModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/thank-you')
    else:
        form = ContributeModelForm()
    return render(request, 'contributors/create_contributor.html', {'form': form})


# def contributor_list_view(request):
#     contributor_obj = CreateContributor.objects.all()
#     return render(request, 'contributors/contributor_list.html', {'contributor_obj': contributor_obj})

class ContributorListView(ListView):
    model = CreateContributor
    paginate_by = 4
    template_name = 'contributors/contributor_list.html'
    ordering = ['-id']
