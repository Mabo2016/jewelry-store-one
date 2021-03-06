# Generated by Django 2.1 on 2018-09-22 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelryapp', '0009_jewelry'),
    ]

    operations = [
        migrations.AddField(
            model_name='jewelry',
            name='detail_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='jewelry',
            name='gemstones_used',
            field=models.CharField(blank=True, choices=[('n', 'Not set'), ('r', 'Ruby'), ('d', 'Diamond'), ('s', 'Saphire'), ('j', 'Jade')], default='n', help_text='Gemstones, like ruby or saphire, used in this item', max_length=1),
        ),
    ]
