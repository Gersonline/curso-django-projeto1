from django.shortcuts import render

def register_View(request):
    return render(request, 'authors/pages/register_view.html')
