from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from finance.views import company_article_list, ChartData, dash, dash_ajax

urlpatterns = [
    url(r'^companies/', company_article_list, name='companies'),
    url(r'^api/chart/data/$', ChartData.as_view(), name='api-chart-data'),
    url(r'^dash/', dash),
    url(r'^_dash', dash_ajax)
    
]