from django.shortcuts import render
from .forms import RegisterForm

def register_View(request):
    if request.POST:
        form = RegisterForm()
    else:
        form = RegisterForm()
    return render(request, 'authors/pages/register_view.html',{
        'form': form
    })
