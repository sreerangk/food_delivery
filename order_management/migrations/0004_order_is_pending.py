# Generated by Django 4.2.7 on 2023-11-18 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0003_orderassignment_order_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_pending',
            field=models.BooleanField(default=True),
        ),
    ]