from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader, Context
from django import forms

#from .templatetags import test
from .forms import Regbaseform
#from .tables import RegbaseTable
#from .tables import Small_table



from .models import Regbase
#from django.db import models
from myapp_1 import models

app_name = 'myapp_1'

#    def do_calculation(self):


class Regbaseform(forms.Form):
#    Purchase_Price =      models.Addnum("Purchase_Price")
    First_Name =      forms.CharField( max_length=50)
    Last_Name =        forms.CharField( max_length=50)
    Mobile_Number =           forms.IntegerField()
    Email =                forms.CharField( max_length=50)


#    Monthly_Interest=     models.IntegerField("Monthly_Interest", null=True)
#    Monthly_Balance=      models.IntegerField("Monthly_Balance", null=True)


    class Meta:
#       db_table = "django_db"
       table = Regbase.objects.all()
       paginate_by = 100

       model = Regbase
       template_name = 'result.html'
       fields = '__all__'
def index(request):

#    return HttpResponse(template.render(context, request))
#    return render(request, 'myapp_1/index.html', context)
    return render(request, 'index.html')

def signup(request): 
#    form = Addnumform(request.GET)
    form = Regbase(request.GET)
#    Regbase.save(Regbaseform)
#    return render(request, 'student.html', {'Addnum':form,}) 
#    return render(request, 'student.html', {'form': form})
    return render(request, 'signup.html')

def login(request): 
#    form = Addnumform(request.GET)
    form = Regbase(request.GET)
#    Regbase.save(Regbaseform)
#    return render(request, 'student.html', {'Addnum':form,}) 
#    return render(request, 'student.html', {'form': form})
    return render(request, 'login.html')

def result(request):

#    if request.method == 'POST':
#    if request.method == 'GET':


#
#        return render(request, "result.html", {"form":form,})

    return renderHttpResponse(request, 'result.html')
    return renderHttpResponse(request, 'result.html')



