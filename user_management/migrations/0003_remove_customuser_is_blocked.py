# Generated by Django 4.2.7 on 2023-11-18 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_blocked',
        ),
    ]