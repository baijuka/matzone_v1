# Generated by Django 3.2.9 on 2021-12-02 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_product_variation_productvariation'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariation',
            name='stock',
            field=models.IntegerField(default=True),
        ),
    ]
