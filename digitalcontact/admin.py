# admin.py

from django.contrib import admin
from django import forms
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponseRedirect
from .models import Contact, TelephoneLine
import csv
import io

@admin.register(TelephoneLine)
class TelephoneLineAdmin(admin.ModelAdmin):
    list_display = ('category', 'lines')
    search_fields = ('category', 'lines')
class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()

class ContactAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'mobile_number', 'email')
    change_list_template = "admin/contact_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-csv/', self.admin_site.admin_view(self.upload_csv), name='upload_csv'),
        ]
        return custom_urls + urls

    def upload_csv(self, request):
        if request.method == 'POST':
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = form.cleaned_data['csv_file']
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)  # Skip the header row
                for row in csv.reader(io_string, delimiter=',', quotechar='"'):
                    Contact.objects.update_or_create(
                        code=row[0],
                        defaults={
                            'name': row[1],
                            'mobile_number': row[2],
                            'email': row[3],
                        }
                    )
                self.message_user(request, "CSV file has been uploaded successfully.")
                return HttpResponseRedirect("../")

        form = CSVUploadForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['upload_form'] = CSVUploadForm()
        return super(ContactAdmin, self).changelist_view(request, extra_context=extra_context)

admin.site.register(Contact, ContactAdmin)
