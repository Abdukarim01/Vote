# Generated by Django 4.0.1 on 2022-03-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0005_registredbotuser_allowed_registredbotuser_checked'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgWrod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('text', models.CharField(max_length=10)),
            ],
        ),
    ]