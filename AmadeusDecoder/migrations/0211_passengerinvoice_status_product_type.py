# Generated by Django 4.0.7 on 2023-01-21 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0210_fee_is_invoiced_othersfee_is_invoiced_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
