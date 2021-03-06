# Generated by Django 2.1 on 2018-09-13 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('house_or_block_identifier', models.CharField(blank=True, max_length=100)),
                ('street_name', models.CharField(blank=True, max_length=100)),
                ('district_name', models.CharField(blank=True, max_length=100)),
                ('city_name', models.CharField(blank=True, max_length=100)),
                ('country_name', django_countries.fields.CountryField(max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
