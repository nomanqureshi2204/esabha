# Generated by Django 2.2 on 2020-02-04 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_msg2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='msg2',
        ),
    ]