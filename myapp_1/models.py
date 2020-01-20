from django.db import models



from django import forms
from django.db.models import Value, Sum


#from my_django18_project.my_django18_project import settings

# Create your models here.

#class Addnum(models.Model):
#    num1 = models.IntegerField("First number")
#    num2 = models.IntegerField("Second number")
#    def __unicode__(self):
#        return "%s plus %s is %s" %(self.num1,self.num2,self.num2+self.num2)

#class Addnumfinal(models.Model):
#    Monthly_Interest=     models.IntegerField("Monthly_Interest", null=True)
#    Monthly_Balance=      models.IntegerField("Monthly_Balance", null=True)

class Regbase(models.Model):
    First_Name =                models.CharField("First Name", max_length=20)
    Last_Name =                models.CharField("Last Name", max_length=20)
    Mobile_Number =                 models.PositiveIntegerField("Mobile Number", null=True)
    Email =          models.CharField("Email", max_length=20)
    def __unicode__(self):
        return "I am %s %s. My email is %s and my mobile number is %s" %(self.First_Name,self.Last_Name,self.Mobile_Number,self.Email)
