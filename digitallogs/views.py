# digitallogs/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Downtime

@login_required
def downtime_list(request):
    downtimes = Downtime.objects.all()
    return render(request, 'downtime_list.html', {'downtimes': downtimes})
