# Generated by Django 3.0.8 on 2020-07-31 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpinghandapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='user_who_owns_this',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_job', to='helpinghandapp.User'),
        ),
    ]
