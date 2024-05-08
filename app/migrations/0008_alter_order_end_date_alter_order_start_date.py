# Generated by Django 5.0.4 on 2024-05-07 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_order_end_date_alter_order_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateTimeField(verbose_name='%Y-%m-%dT%H:%M'),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(verbose_name='%Y-%m-%dT%H:%M'),
        ),
    ]
