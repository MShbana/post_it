# Generated by Django 2.2.3 on 2019-07-27 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20190727_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='updated',
            new_name='date_updated',
        ),
    ]