from django.shortcuts import render
from django.utils import timezone

import reserve
from .models import Reserve
from django.utils import timezone
#from .forms import ReserveForm

def index(request):
    reserves = Reserve.objects.filter(published_date=timezone.now()).order_by('published_date')
    return render(request, 'reserve/index.html', {'reserve': reserves})

#def reserve_new(request):
    #form = ReserveForm()
    #return render (request, 'reserve/index.html', {'form': form})