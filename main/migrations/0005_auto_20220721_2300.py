# Generated by Django 3.2.9 on 2022-07-21 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220721_2253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='latest_episode',
            old_name='Episode_1',
            new_name='Episode',
        ),
        migrations.RemoveField(
            model_name='latest_episode',
            name='Episode_2',
        ),
    ]