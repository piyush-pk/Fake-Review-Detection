# Generated by Django 4.0.2 on 2022-02-09 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detect', '0002_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]