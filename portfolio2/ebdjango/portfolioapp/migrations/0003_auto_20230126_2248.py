# Generated by Django 2.2 on 2023-01-26 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0002_auto_20230126_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='summary',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='skills',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]