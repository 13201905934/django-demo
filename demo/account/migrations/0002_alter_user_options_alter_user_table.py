# Generated by Django 4.2.13 on 2024-06-28 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户信息'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
