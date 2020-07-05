from django.shortcuts import render


def index(request):
    return render(request, 'prof/index.html')


def work_organica(request):
    return render(request, 'prof/work-organica.html')


def work_apollo(request):
    return render(request, 'prof/work-apollo.html')


def site_portfolio(request):
    return render(request, 'prof/site-portfolio.html')