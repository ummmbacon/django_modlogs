# Generated by Django 4.1.5 on 2023-01-24 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modlogs', '0010_alter_modlog_mod_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modlog',
            name='mod_item',
            field=models.TextField(blank=True, null=True),
        ),
    ]
