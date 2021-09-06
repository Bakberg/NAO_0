from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


def news (request):
    news = New.objects.all()
    return render(request, 'main/news.html', {'news': news})


class Test(TemplateView):
    template_name = 'news.html'

    pass
