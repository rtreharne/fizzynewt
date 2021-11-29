# Generated by Django 3.2.8 on 2021-11-29 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.FloatField(default=12),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
