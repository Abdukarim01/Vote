# Generated by Django 4.0.1 on 2022-03-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_alter_places_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='vote',
            field=models.PositiveIntegerField(default=0, verbose_name='Bu joyga ovoz berish'),
        ),
    ]