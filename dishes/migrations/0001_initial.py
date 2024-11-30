# Generated by Django 5.1.2 on 2024-10-29 03:12

import dishes.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dish_votes',
            fields=[
                ('dish_Id', models.AutoField(primary_key=True, serialize=False)),
                ('d_Name', models.CharField(max_length=100)),
                ('d_Description', models.CharField(max_length=1000)),
                ('d_Ingredients', models.CharField(max_length=500)),
                ('d_Price', models.IntegerField(blank=True)),
                ('d_Photo', models.FileField(upload_to=dishes.models.user_directory_path, verbose_name='')),
                ('d_Type', models.CharField(max_length=10)),
                ('v_Date', models.DateField(auto_now_add=True)),
                ('d_Votes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dish_votes',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotel_Id', models.AutoField(primary_key=True, serialize=False)),
                ('h_Name', models.CharField(max_length=100)),
                ('h_Address', models.CharField(max_length=500)),
                ('h_Contact', models.CharField(blank=True, max_length=15, null=True)),
                ('h_Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('h_Photo', models.ImageField(blank=True, null=True, upload_to='hotels')),
            ],
            options={
                'db_table': 'hotels',
            },
        ),
        migrations.CreateModel(
            name='dishes',
            fields=[
                ('dish_Id', models.AutoField(primary_key=True, serialize=False)),
                ('d_Name', models.CharField(max_length=100)),
                ('d_Description', models.CharField(max_length=1000)),
                ('d_Ingredients', models.CharField(max_length=500)),
                ('d_Price', models.IntegerField()),
                ('d_Photo', models.FileField(upload_to=dishes.models.user_directory_path, verbose_name='')),
                ('d_Type', models.CharField(max_length=10)),
                ('d_Add_Date', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='dishes.hotel')),
            ],
            options={
                'db_table': 'dishes',
            },
        ),
    ]
