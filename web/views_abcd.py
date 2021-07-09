from django.core.paginator import Paginator
from django.db import models
from django.shortcuts import render, get_list_or_404
from django.views.generic import DetailView, ListView

from .models_abcd import Component, Report, TimeSeries

class TimeSeriesList(ListView):
    
    """List of all time series"""
    
    model = TimeSeries
    template_name = "web/abcd/time_series_list.html"
    paginate_by = 5

    def get(self, request):
        
        context = {"ts_list": TimeSeries.objects.all()}
        return render(request, self.template_name, context)

class ReportList(ListView):
    
    """List all reports of a time series"""
    
    model = Report
    template_name = "web/abcd/report_list.html"
    paginate_by = 10
    
    def get(self, request, time_series):
        
        report_list = Report.objects.filter(time_series=time_series)
        
        # TODO: pagination
        # paginator = Paginator(queryset, self.paginate_by)
        # page = request.GET.get('page')
        # page = 1 if page is None else page 
        
        context = {"report_list": report_list}
        
        return render(request, self.template_name, context)
        

class ReportDetail(DetailView):
    
    model = Report
    template_name = "web/abcd/detail_full.html"
    
    
    def get(self, request, report_id):
        
        
        list_report = Report.objects.filter(id=report_id)
        report = list_report[0]
        
        components = Component.objects.filter(report_id=report)
        
        context = {"components": components, "mav_data":1., "report":report}
        
        return render(request, self.template_name, context)
    


