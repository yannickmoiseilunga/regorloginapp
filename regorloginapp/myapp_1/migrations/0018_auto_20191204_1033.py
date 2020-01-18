# Generated by Django 2.2.7 on 2019-12-04 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_1', '0017_auto_20191130_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='addnum',
            name='Bond_Term1',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='addnum',
            name='Interest',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='addnum',
            name='Loan_Amount',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='addnum',
            name='R',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='addnum',
            name='X',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='addnum',
            name='Age',
            field=models.PositiveIntegerField(null=True, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='addnum',
            name='Bond_Term',
            field=models.PositiveIntegerField(verbose_name='Bond_Term'),
        ),
        migrations.AlterField(
            model_name='addnum',
            name='Deposit_Paid',
            field=models.PositiveIntegerField(verbose_name='Deposit_Paid'),
        ),
        migrations.AlterField(
            model_name='addnum',
            name='Fixed_Interest_Rate',
            field=models.PositiveIntegerField(verbose_name='Fixed_Interest_Rate'),
        ),
        migrations.AlterField(
            model_name='addnum',
            name='Purchase_Price',
            field=models.PositiveIntegerField(verbose_name='Purchase_Price'),
        ),
    ]