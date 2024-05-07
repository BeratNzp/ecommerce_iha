# Generated by Django 5.0.4 on 2024-05-07 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('RECEIVED', 'Received'), ('DELAYED', 'Delayed'), ('RETURNED', 'Returned')], default='Pending'),
        ),
    ]
