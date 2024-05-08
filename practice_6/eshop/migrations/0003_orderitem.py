# Generated by Django 5.0.3 on 2024-03-11 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0002_remove_cart_products_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='eshop.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.product')),
            ],
        ),
    ]
