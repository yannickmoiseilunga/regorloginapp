# Generated by Django 2.2.7 on 2019-11-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_1', '0003_auto_20191126_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addnum',
            name='Age',
            field=models.IntegerField(null=True, verbose_name='Age'),
        ),
        migrations.AlterModelTable(
            name='addnum',
#            table="django_db",
#            table="",'django_db'
            table='django_db',
        ),
    ]
