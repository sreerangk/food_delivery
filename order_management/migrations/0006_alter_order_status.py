# Generated by Django 4.2.7 on 2023-11-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0005_order_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('CANCELLED', 'Cancelled'), ('DELIVERED', 'Delivered'), ('CONFIRM-DELIVERED', 'confirm-delivered')], default='PENDING', max_length=50),
        ),
    ]
