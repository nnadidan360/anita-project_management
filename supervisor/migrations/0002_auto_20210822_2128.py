# Generated by Django 3.0.2 on 2021-08-22 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_project_user'),
        ('supervisor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='checkStats',
            new_name='checkStat',
        ),
        migrations.AlterModelOptions(
            name='checkstat',
            options={},
        ),
    ]
