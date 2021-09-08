import os
import pickle

from django.core.paginator import Paginator
from django.db import models
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.conf import settings
import mlflow


from .models_abcd import Report, TimeSeries

REPORT_DIR = os.path.join(settings.STATICFILES_DIRS[0], "upload/AutomaticNews")
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
    
    mlflow_client = mlflow.tracking.MlflowClient(settings.MLFLOW_URI)
    
    def get(self, request, report_id):
        
        
        list_report = Report.objects.filter(id=report_id)
        report = list_report[0]

        local_dir = self.download_artifacts(run_id=report.run_id,
                                storage_dir=REPORT_DIR)
        
        component_file = os.path.join(local_dir, "components.pkl")
        components = load_components(component_file)
        context = {"components":components, "mav_data":1, "report": report} 
        return render(request, self.template_name, context)
    
    def download_artifacts(self, run_id, storage_dir):
        
        local_dir = os.path.join(storage_dir, run_id)
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
            local_dir = self.mlflow_client.download_artifacts(run_id, 
                                                         path=".",
                                                         dst_path=local_dir)
            print(f"Download artifact to {local_dir}") 
        else:
            print(f"Experiment is already persisted. No need to download")           
        return local_dir
    
def load_components(path):
    
    """Return a list of dictionaries"""
    
    with open(path, 'rb') as f:
        components = pickle.load(f)
    
    return components


    
    


