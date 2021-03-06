# Generated by Django 3.1.5 on 2021-02-18 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20210218_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collector_id', models.CharField(max_length=50, null=True, verbose_name='Collector ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('mobile', models.CharField(max_length=50, null=True, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='EMail')),
                ('date_of_joining', models.DateField(verbose_name='Date of Joining')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='Address')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='City')),
                ('state', models.CharField(max_length=50, null=True, verbose_name='State')),
                ('pincode', models.CharField(max_length=50, null=True, verbose_name='Pincode')),
                ('company_name', models.CharField(max_length=50, null=True, verbose_name='Company Name')),
                ('bank_account_number', models.CharField(max_length=50, null=True, verbose_name='Bank Account Number')),
                ('ifsc_code', models.CharField(max_length=50, null=True, verbose_name='IFSC COde')),
                ('branch_addresss', models.CharField(max_length=50, null=True, verbose_name='Branch Address')),
                ('branch_name', models.CharField(max_length=50, null=True, verbose_name='Branch Name')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50, null=True, verbose_name='')),
                ('amount', models.CharField(max_length=50, null=True, verbose_name='Amount')),
                ('transacton_id', models.CharField(max_length=50, null=True, verbose_name='Transaction ID')),
                ('transaction_datetime', models.DateTimeField(verbose_name='Date and Time')),
                ('status', models.CharField(max_length=50, null=True, verbose_name='Status')),
                ('circle_name', models.CharField(max_length=50, null=True, verbose_name='')),
                ('plan_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.createplans')),
                ('stb_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.stb')),
            ],
        ),
    ]
