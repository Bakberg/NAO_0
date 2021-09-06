from pyexpat.errors import messages
from django.core import mail
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from news.models import *
from coment.forms import *
from coment.models import *


def glav (request):
    news = New.objects.all()
    error = ''
    if request.method == 'POST':
        form = COMENTForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            error = 'Форма заполнен не верна'

    form = COMENTForm

    return render(request, 'main/glav.html', {'news': news, 'form': form, 'error': error})

def kategory (request):
    return render(request, 'main/kategory.html')

def news (request):
    news = New.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title']
    return render(request, 'main/news.html', {'news': news, 'filter_backends': filter_backends, 'filter_fields': filter_fields})

def otziv (request):
    otzivs = Coment.objects.all()
    return render(request, 'main/otziv.html', {'otzivs': otzivs} )

def gilim (request):
    return render(request, 'main/gilim.html')

def bilim (request):
    return render(request, 'main/bilim.html')

def Innovacia (request):
    return render(request, 'main/Innovacia.html')

def Adisteme (request):
    dropdown_ones = Dropdown_one.objects.all()
    return render(request, 'main/Adisteme.html', {'dropdown_ones': dropdown_ones})

def st_1 (request):
    return render(request, 'main/st_1.html')

def st_2 (request):
    return render(request, 'main/st_2.html')

def news_2 (request):
    news = New.objects.all()
    return render(request, 'main/news_2.html', {'news': news})

def base (request):
    return render(request, 'main/base.html')

class Test(TemplateView):
    template_name = 'glav.html'

    pass