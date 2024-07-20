import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Downtime, Serveraccess

@login_required
def downtime_list(request):
    downtimes = Downtime.objects.all()
    serveraccesses = Serveraccess.objects.all()

    # Pagination for Downtime logs
    downtime_paginator = Paginator(downtimes, 5)
    downtime_page_number = request.GET.get('downtime_page')
    downtime_page_obj = downtime_paginator.get_page(downtime_page_number)

    # Pagination for Server Access logs
    serveraccess_paginator = Paginator(serveraccesses, 5)
    serveraccess_page_number = request.GET.get('serveraccess_page')
    serveraccess_page_obj = serveraccess_paginator.get_page(serveraccess_page_number)

    context = {
        'downtime_page_obj': downtime_page_obj,
        'serveraccess_page_obj': serveraccess_page_obj,
    }
    return render(request, 'downtime_list.html', context)

@login_required
def export_downtimes_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="downtimes.csv"'

    writer = csv.writer(response)
    writer.writerow(['SN', 'Date and Time', 'System/Channel Name', 'Reason', 'Downtime Total Time', 'Impact'])

    downtimes = Downtime.objects.all()
    for downtime in downtimes:
        writer.writerow([downtime.sn, downtime.datetime, downtime.system_channel_name, downtime.reason, downtime.downtime_total_time, downtime.impact])

    return response

@login_required
def export_serveraccess_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="serveraccess.csv"'

    writer = csv.writer(response)
    writer.writerow(['SN', 'Date and Time', 'Server Name', 'Purpose', 'Access by', 'Provided by', 'Time'])

    serveraccesses = Serveraccess.objects.all()
    for log in serveraccesses:
        writer.writerow([log.sn, log.datetime, log.server_name, log.purpose, log.access_by, log.provided_by, log.time])

    return response
