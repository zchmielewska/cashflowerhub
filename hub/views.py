from django.shortcuts import render


def models_view(request):
    return render(request, 'models.html')


def runs_view(request):
    return render(request, 'runs.html')


def documentation_view(request):
    return render(request, 'documentation.html')
