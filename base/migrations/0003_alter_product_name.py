# Generated by Django 4.0 on 2021-12-26 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_order_shippingprice_alter_order_taxprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default='/sample.jpg', max_length=200, null=True),
        ),
    ]
