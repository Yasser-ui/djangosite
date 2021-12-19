from django.shortcuts import render
from .models import Reserve

def index(request):
    return render(request, 'reserve/index.html', {})