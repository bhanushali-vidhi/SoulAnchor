# Generated by Django 5.0.3 on 2024-03-30 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey_filled',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]