# Generated by Django 3.2.9 on 2021-12-13 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20211213_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='productsize',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
