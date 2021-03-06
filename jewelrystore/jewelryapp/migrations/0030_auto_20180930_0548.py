# Generated by Django 2.1 on 2018-09-30 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelryapp', '0029_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, help_text='The total price of all items ordered by this order instance', max_digits=12),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, help_text='The total price of all items in the shopping cart', max_digits=12),
        ),
    ]
