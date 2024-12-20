# Generated by Django 5.1.2 on 2024-10-29 03:12

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
            name='user_votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_Id', models.CharField(max_length=100)),
                ('dish_Id', models.CharField(max_length=100)),
                ('dish_Name', models.CharField(max_length=100)),
                ('v_Date', models.DateField(auto_now_add=True)),
                ('v_Time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_votes',
            },
        ),
        migrations.CreateModel(
            name='f_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_Email', models.CharField(max_length=100)),
                ('user_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
