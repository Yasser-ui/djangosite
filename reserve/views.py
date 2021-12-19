from django.shortcuts import render
from django.utils import timezone

import reserve
from .models import Reserve

def index(request):
    reserves = 
    return render(request, 'reserve/index.html', {'reserve': reserves})