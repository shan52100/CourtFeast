# Generated by Django 5.1.2 on 2024-10-29 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='h_Address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
