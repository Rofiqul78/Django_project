# Generated by Django 4.2.7 on 2023-12-12 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_blogtables_created_at_blogtables_imagefield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogtables',
            name='ImageField',
        ),
    ]