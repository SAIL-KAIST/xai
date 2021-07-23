
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
    image_folder = models.ImageField(upload_to="AutomaticNews/") # point to the folder that the generated html need
    
    
    def __str__(self) -> str:
        return self.title
    

class Component(models.Model):
    
    report_id = models.ForeignKey(Report, on_delete=models.CASCADE)
    
    # order of this component
    i = models.IntegerField()
    # statistic fields
    var = models.FloatField()
    
    mae = models.FloatField()
    mae_reduction = models.FloatField()
    
    # cumulative statistic fields
    cum_var = models.FloatField()
    cum_res_var = models.FloatField()
    
    
    # some more stastic for model checking
    mmd_p_value=models.FloatField()
    qq_d_max = models.FloatField()
    qq_d_min = models.FloatField()
    acf_min_loc = models.FloatField()
    acf_min = models.FloatField()
    pxx_max_loc = models.FloatField()
    pxx_max = models.FloatField() 
    
    # figure:
    fit= models.ImageField(upload_to="AutomaticNews", default='fit_0.png')
    extrap= models.ImageField(upload_to="AutomaticNews",default='extrap_0.png')
    sample= models.ImageField(upload_to="AutomaticNews",default='sample_0.png')
    cum_fit= models.ImageField(upload_to="AutomaticNews",default='cum_fit_0.png')
    cum_extrap= models.ImageField(upload_to="AutomaticNews",default='cum_extrap_0.png')
    cum_sample= models.ImageField(upload_to="AutomaticNews",default='cum_sample_0.png')
    anti_res= models.ImageField(upload_to="AutomaticNews",default='anti_res_0.png')
    
    
    # description fields
    summary = models.TextField()
    full_desc = models.TextField()
    extrap_desc = models.TextField()
    
    def __str__(self) -> str:
        return self.summary