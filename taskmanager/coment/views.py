from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import *

def vopros (request):
    error = ''
    if request.method == 'POST':
        form = COMENTForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            error = 'Форма заполнен не верна'

    form = COMENTForm

    return render(request, 'main/vopros.html', {'form': form, 'error': error})


class Test(TemplateView):
    template_name = 'vopros.html'

    pass