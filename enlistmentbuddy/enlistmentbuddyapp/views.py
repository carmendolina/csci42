from django.shortcuts import render, redirect

from django.http import HttpResponse

#forms
from .forms import IndexCardForm

from .models import IndexCard

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

#insert functions here
def index(request):
    return redirect('index_card')


def index_card_view(request):
    form = IndexCardForm(request.POST)
    classes = IndexCard.objects.all()
    if request.method == 'POST':
    # Checking if the inputs are valid
        if form.is_valid():
            form.save()
            return render(
                'Code: {} Section: {} Venue: {} Professor: {}'.format(
                # Getting data from our form that have been validated
                form.cleaned_data['code'],
                form.cleaned_data['section'],
                form.cleaned_data['venue'],
                form.cleaned_data['professor']
                )
            )
    else:
        form = IndexCardForm()
    return render(request, 'index.html', {'form': form, 'class_info': classes})
