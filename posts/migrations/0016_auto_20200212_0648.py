# Generated by Django 2.2 on 2020-02-12 06:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20200212_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cr_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 12, 6, 48, 7, 386081, tzinfo=utc)),
        ),
    ]