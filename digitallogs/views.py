import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Downtime, Serveraccess, TechnicalSupportLog, TaskLog


@login_required
def adminpanel(request):
    return render(request, 'adminpanel.html')

@login_required
def downtime_list(request):
    downtimes = Downtime.objects.all().order_by('-datetime')
    #serveraccesses = Serveraccess.objects.all().order_by('-datetime')

    # Pagination for Downtime logs
    downtime_paginator = Paginator(downtimes, 5)
    downtime_page_number = request.GET.get('downtime_page')
    downtime_page_obj = downtime_paginator.get_page(downtime_page_number)

    # Pagination for Server Access logs
    #serveraccess_paginator = Paginator(serveraccesses, 5)
    #serveraccess_page_number = request.GET.get('serveraccess_page')
    #serveraccess_page_obj = serveraccess_paginator.get_page(serveraccess_page_number)

    context = {
        'downtime_page_obj': downtime_page_obj,
        #'serveraccess_page_obj': serveraccess_page_obj,
    }
    return render(request, 'downtime_list.html', context)

@login_required
def export_downtimes_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="downtimes.csv"'

    writer = csv.writer(response)
    writer.writerow(['SN', 'Date and Time', 'System/Channel Name', 'Reason', 'Downtime Total Time', 'Impact'])

    downtimes = Downtime.objects.all().order_by('-datetime')
    for downtime in downtimes:
        writer.writerow([downtime.sn, downtime.datetime, downtime.system_channel_name, downtime.reason, downtime.downtime_total_time, downtime.impact])

    return response

@login_required
def export_serveraccess_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="serveraccess.csv"'

    writer = csv.writer(response)
    writer.writerow(['SN', 'Date and Time', 'Server Name', 'Purpose', 'Access by', 'Provided by', 'Time'])

    serveraccesses = Serveraccess.objects.all().order_by('-datetime')
    for log in serveraccesses:
        writer.writerow([log.sn, log.datetime, log.server_name, log.purpose, log.access_by, log.provided_by, log.time])

    return response

@login_required
def serverlog_list(request):
    serveraccesses = Serveraccess.objects.all().order_by('-datetime')

    # Pagination for Server Access logs
    serveraccess_paginator = Paginator(serveraccesses, 5)
    serveraccess_page_number = request.GET.get('serveraccess_page')
    serveraccess_page_obj = serveraccess_paginator.get_page(serveraccess_page_number)

    context = {
        'serveraccess_page_obj': serveraccess_page_obj,
    }
    return render(request, 'serverlog.html', context)

@login_required
def technical_log_list(request):
    tech_logs = TechnicalSupportLog.objects.all().order_by('-date')
    paginator = Paginator(tech_logs, 5)  # Show 5 logs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'technicallog.html', context)

@login_required
def export_technical_logs_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="technical_support_logs.csv"'

    writer = csv.writer(response)
    writer.writerow(['SN', 'Issue No', 'Date', 'Category', 'Requested by', 'Issue logged to', 'Issue Description', 'Reference code', 'Handling person', 'Status'])

    tech_logs = TechnicalSupportLog.objects.all()
    for log in tech_logs:
        writer.writerow([log.sn, log.issue_no, log.date, log.category, log.requested_by, log.issue_logged_to, log.issue_description, log.reference_code, log.handling_person, log.status])

    return response

@login_required
def tasklog_list(request):
    tasklogs = TaskLog.objects.all().order_by('-assigned_date')
    paginator = Paginator(tasklogs, 5)  # Show 5 logs per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'tasklog_page_obj': page_obj,
    }
    return render(request, 'tasklog.html', context)