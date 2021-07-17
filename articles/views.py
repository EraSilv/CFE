from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'mainbodytx.html')

def desert(request):
    return render(request, 'desert.html')