# Generated by Django 3.2.8 on 2021-12-08 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_alter_school_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
