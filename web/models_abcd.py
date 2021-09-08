
from django.db import models

class TimeSeries(models.Model):
    
    short_name = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    

class Report(models.Model): 
    """
    Automatic generated reported from ABCD in English
    """
    
    time_series = models.ForeignKey(TimeSeries, on_delete=models.PROTECT)
    
    title = models.CharField(max_length=100)
    datetime = models.DateTimeField() # when to save to data base?
    run_id = models.CharField(max_length=100)
    
    
    def __str__(self) -> str:
        return self.title