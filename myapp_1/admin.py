from django.contrib import admin

from . import models
from .models import Regbase

admin.site.site_header = " Bond Calculator admin"
admin.site.site_title = " Bond Calculator admin area"
admin.site.index_title = " Welcome to the Bond Calculator admin area"

# Register your models here.

admin.site.register(models.Regbase)
#admin.site.register(models.myapp_1)
