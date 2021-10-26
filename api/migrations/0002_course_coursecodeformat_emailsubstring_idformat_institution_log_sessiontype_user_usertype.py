# Generated by Django 3.1.5 on 2021-02-01 20:51

from django.db import migrations, models
import django.db.models.deletion
import regex_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SessionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=16)),
                ('desceription', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('user_id', regex_field.fields.RegexField(max_length=128)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.institution')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newt_code', models.CharField(max_length=128)),
                ('start', models.DateTimeField()),
                ('finish', models.DateTimeField()),
                ('message', models.TextField(default=False, max_length=10000, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.course')),
                ('session_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.sessiontype')),
            ],
        ),
        migrations.CreateModel(
            name='IdFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regex', regex_field.fields.RegexField(max_length=128)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.institution')),
            ],
        ),
        migrations.CreateModel(
            name='EmailSubstring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('substring', models.CharField(max_length=128)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.institution')),
            ],
        ),
        migrations.CreateModel(
            name='CourseCodeFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regex', regex_field.fields.RegexField(max_length=128)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.institution')),
            ],
        ),
    ]