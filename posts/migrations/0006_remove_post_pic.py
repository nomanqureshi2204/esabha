# Generated by Django 2.2 on 2020-02-06 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200206_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pic',
        ),
    ]
