from django.db import models
from . import tables



from django import forms

from .models import Regbase





#from my_django18_project.my_django18_project import settings

context = {
'query_results' : Regbase.objects.all(),

'First_Name ':  Regbase.First_Name,
'Last_Name ':  Regbase.Last_Name,
'Mobile_Number': Regbase.Mobile_Number,
'Email': Regbase.Email,

#'solution':solution,
#'final_solution':final_solution,
}

class AddnumTable(tables.Table):
    table = Regbase.objects.all()
    table = tables.Column(order_by=("Purchase_Price", "Deposit_Paid", "Monthly_Interest", "Monthly_Balance"))
    tableoth  = tables.Column(orderable=False)

#    name = tables.LinkColumn("result", args=[A("pk")])
    paginate_by = 100
    paginator = LazyPaginator(range(10000), 10)
    class Meta:
#        table = "django_db"
        table = Regbase.objects.all()
        model = Regbase
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "paleblue"}
        paginate_by = 100
        paginator = LazyPaginator(range(10000), 10)
        fields = ("Purchase_Price", "Deposit_Paid", "Bond_Term", "Fixed_Interest_Rate", "Monthly_Interest", "Monthly_Balance", )

table = AddnumTable(context)