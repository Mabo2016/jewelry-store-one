# Generated by Django 2.1 on 2018-09-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jewelryapp', '0008_auto_20180920_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jewelry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Required. E.g. Stainless Steel Mixed Color Pendant', max_length=100, null=True)),
                ('date_time_added', models.DateField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('metallic_finish', models.CharField(blank=True, choices=[('n', 'Not set'), ('n', 'Common'), ('t', 'Stainless Steel'), ('s', 'Silver'), ('g', 'Gold'), ('r', 'Rose Gold'), ('p', 'Platinum')], default='n', help_text='Metal the jewelry is made from', max_length=1)),
                ('availability', models.CharField(blank=True, choices=[('o', 'Out of stock'), ('a', 'Available')], default='a', help_text='Availability for purchase', max_length=1)),
            ],
        ),
    ]
