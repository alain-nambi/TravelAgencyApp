# Generated by Django 4.0.6 on 2023-03-07 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0235_history'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='passengerinvoice',
        #     name='status',
        #     field=models.CharField(max_length=100, null=True),
        # ),
        migrations.AddField(
            model_name='ticket',
            name='is_deposit',
            field=models.BooleanField(default=0),
        ),
    ]
