# Generated by Django 2.0.3 on 2018-04-29 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180428_1609'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ViewedNum',
            new_name='ReadNum',
        ),
        migrations.RenameField(
            model_name='readnum',
            old_name='viewed_num',
            new_name='read_num',
        ),
    ]