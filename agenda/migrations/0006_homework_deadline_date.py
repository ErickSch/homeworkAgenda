# Generated by Django 4.1.1 on 2022-09-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_alter_homework_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='deadline_date',
            field=models.DateField(null=True),
        ),
    ]
