# Generated by Django 3.1.5 on 2021-02-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_node_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50, null=True, verbose_name='Make')),
                ('DOP', models.DateField(verbose_name='Date Of Purchase')),
                ('issue_date', models.DateField(verbose_name='Issue Date')),
                ('type1', models.CharField(choices=[('1', 'Prepaid'), ('2', 'Postpaid'), ('3', 'Complementary')], default='0', max_length=50, verbose_name='Type')),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default='0', max_length=50, verbose_name='Status')),
                ('router_type', models.CharField(choices=[('1', 'Data'), ('2', 'Wifi'), ('3', 'Dual Band')], default='0', max_length=50, verbose_name='Router Type')),
                ('remark', models.TextField(verbose_name='Remark')),
                ('model_number', models.CharField(max_length=50, null=True, verbose_name='Model Number')),
                ('mac_id', models.CharField(max_length=50, null=True, verbose_name='MAC ID')),
                ('ip_address', models.CharField(max_length=50, null=True, verbose_name='IP Address')),
            ],
        ),
    ]
