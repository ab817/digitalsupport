# digitallogs/views.py

import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Downtime

@login_required
def downtime_list(request):
    downtimes = Downtime.objects.all()
    paginator = Paginator(downtimes, 5)  # Show 5 downtimes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'downtime_list.html', {'page_obj': page_obj})

@login_required
def export_downtimes_csv(request):
    downtimes = Downtime.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="downtimes.csv"'

    writer = csv.writer(response)
    writer.writerow(['SN', 'Date and Time', 'System/Channel Name', 'Reason', 'Downtime Total Time', 'Impact'])

    for downtime in downtimes:
        writer.writerow([downtime.sn, downtime.datetime, downtime.system_channel_name, downtime.reason, downtime.downtime_total_time, downtime.impact])

    return response
