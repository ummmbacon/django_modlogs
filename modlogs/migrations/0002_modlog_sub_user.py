# Generated by Django 4.1.5 on 2023-01-19 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modlogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modlog',
            name='sub_user',
            field=models.CharField(default='Not Specified', max_length=25),
        ),
    ]
