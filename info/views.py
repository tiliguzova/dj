from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'index.html')


def read_pizza(request):
    return render(request, 'all.html')


def contest(request):
    return render(request, 'contest.html')
