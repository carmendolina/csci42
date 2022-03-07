from django.shortcuts import render, redirect

from django.http import HttpResponse

#forms
from .forms import IndexCardForm

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

#insert functions here
def index(request):
    return HttpResponse('Hello World! This came from the index view')


def index_card_view(request):
    # Checking for POST request
    if request.method == 'POST':
        # Creating a Form object
        form = IndexCardForm(request.POST)
    # Checking if the inputs are valid
        if form.is_valid():
            return HttpResponse(
                'Hello {} from Section {}'.format(
                # Getting data from our form that have been validated
                form.cleaned_data['name'],
                form.cleaned_data['section']
                )
            )
    else:
        form = IndexCardForm()
    return render(request, 'index.html', {'form': form})