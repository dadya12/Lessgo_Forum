# Generated by Django 5.0.6 on 2024-08-03 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]
