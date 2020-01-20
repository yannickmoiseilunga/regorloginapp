from django.contrib import admin
from django.urls import include, path, re_path

from django.conf.urls import url

#from myapp_1.views import IndexView, StudentView, ResultsView

from . import views

admin.autodiscover()
app_name = 'myapp_1'

urlpatterns = [

    path('myapp_1/', include('myapp_1.urls')), 
    path('admin/', admin.site.urls),


]