# Generated by Django 5.1 on 2024-08-29 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_review_comment_remove_review_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
