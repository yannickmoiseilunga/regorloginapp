
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader, Context
from django.forms import ModelForm
#, forms
#from django.forms import *
#from myapp_1 import *
from myapp_1 import forms
from myapp_1.forms import Addnum


class Addnumform(forms.Addnum):
#class Addnumform(ModelForm):
     class Meta:
        model = Addnum

Class IndexView(TemplateView)
    template_name = "index.html"

Class StudentView(TemplateView)
    template_name = "student.html"

Class ResultsView(TemplateView)
    template_name = "result.html"



#def index(request):
#    latest_entry_list =  Addnum.objects.order_by('Name')[:5]
#    template = loader.get_template('myapp_1/index.html')
#    context = {
#        'latest_entry_list': latest_entry_list,
#    }
#    return render(request, 'myapp_1/index.html', context)



#def index(request):

#    return render(request, "index.html", {})

#def student(request):  

def student(request, Addnum_id): 
    if request.POST:
        form = Addnumform(request.POST)
        if form.is_valid:
            f = form.save()
            return HttpResponseRedirect("/student/ %d/" %f.id)
    else:
        form = Addnumform()
#    return render_to_response('student.html',context_instance=RequestContext(request, {"form":form,}))

#    return render(request, "myapp_1/student.html", {"form":form,})
    return render(request, "myapp_1/student.html", {'Addnum':Addnum})

def result(request, Addnum_id):
#def result(request, Purchase_Price, Deposit_Paid, Bond_Term, Fixed_Interest_Rate, Name):
   context = {'Purchase_Price' : Purchase_Price, 'Deposit_Paid' : Deposit_Paid, 'Bond_Term' : Bond_Term, 'Fixed_Interest_Rate' : Fixed_Interest_Rate, 'Name' : Name}

   if request.method == "POST":
      MyAddnum = Addnum(request.POST)

      if MyAddnum.is_valid():
         username = MyAddnum.cleaned_data['username']
         Purchase_Price = MyAddnum.cleaned_data['Purchase_Price']
         Deposit_Paid = MyAddnum.cleaned_data['Deposit_Paid']
         Bond_Term = MyAddnum.cleaned_data['Bond_Term']
         Fixed_Interest_Rate = MyAddnum.cleaned_data['Fixed_Interest_Rate']
         Name = MyAddnum.cleaned_data['Name']
   else:
      MyAddnum = Addnum()
   return render(request, 'myapp_1/result.html', context)
#{"Purchase_Price" : Purchase_Price}, {"Deposit_Paid" : Deposit_Paid}, {"Bond_Term" : Bond_Term}, {"Fixed_Interest_Rate" : Fixed_Interest_Rate}, {"Name" : Name})


#def result(request,id):
#    nums = Add.num.objects.get(pk=id)
#    return render_to_response('student.html', context_instance=RequestContext(request, {"nums":nums, }))

#    return render(request, "result.html", {"nums":nums,})
