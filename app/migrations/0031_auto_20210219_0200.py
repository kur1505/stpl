# Generated by Django 3.1.5 on 2021-02-18 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_remove_profile_act'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='profile_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
    ]
