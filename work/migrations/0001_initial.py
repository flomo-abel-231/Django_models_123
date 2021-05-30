# Generated by Django 3.2.3 on 2021-05-29 10:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=400)),
                ('year_of_graduation', models.DateField(default=datetime.datetime.today)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('postal_code', models.IntegerField()),
                ('date', models.DateField(blank=True)),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.student')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=400)),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.student')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.student')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('faculty', models.CharField(blank=True, max_length=700)),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.student')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500)),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.student')),
            ],
        ),
    ]