# Generated by Django 4.2.7 on 2023-11-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0004_order_is_pending'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='otp',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
