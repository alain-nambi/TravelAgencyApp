# Generated by Django 4.0.7 on 2023-01-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0211_passengerinvoice_status_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='othersfee',
            name='product_id',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
