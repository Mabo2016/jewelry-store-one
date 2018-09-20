# Generated by Django 2.1 on 2018-09-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelryapp', '0004_auto_20180916_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='delivery_address',
            field=models.CharField(blank=True, help_text='Required. House or Block number, street number or name, district name', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Required. 10 digits only. E.g 0552233444', max_length=10, null=True),
        ),
    ]
