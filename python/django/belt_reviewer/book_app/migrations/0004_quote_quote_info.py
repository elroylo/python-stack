# Generated by Django 3.0.8 on 2020-07-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0003_auto_20200727_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='quote_info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
