# Generated by Django 3.2.9 on 2021-12-13 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20211213_2142'),
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='productsize',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='products.productvariation'),
            preserve_default=False,
        ),
    ]
