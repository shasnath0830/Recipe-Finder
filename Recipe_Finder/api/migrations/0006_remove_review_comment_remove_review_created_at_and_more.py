# Generated by Django 5.1 on 2024-08-29 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='review',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewer_name',
        ),
    ]
