# Generated by Django 4.1.1 on 2022-09-19 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_homework_deadline_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='deadline_date',
        ),
    ]
