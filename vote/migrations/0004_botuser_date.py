# Generated by Django 4.0.1 on 2022-03-19 16:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_remove_botuser_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 3, 19, 16, 36, 39, 57257, tzinfo=utc)),
            preserve_default=False,
        ),
    ]