# Generated by Django 5.0.6 on 2024-05-31 11:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('salary', models.IntegerField(default=0)),
                ('company', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('job_type', models.CharField(choices=[('FT', 'Полный рабочий день'), ('PT', 'Частичная занятость'), ('CT', 'Контракт'), ('FL', 'Фриланс')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UsersJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
