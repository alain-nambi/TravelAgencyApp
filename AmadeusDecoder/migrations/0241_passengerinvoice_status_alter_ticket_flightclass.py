# Generated by Django 4.1.7 on 2023-03-24 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0240_passengerinvoice_is_archived_passengerinvoice_status'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='passengerinvoice',
        #     name='status',
        #     field=models.CharField(max_length=100, null=True),
        # ),
        migrations.AlterField(
            model_name='ticket',
            name='flightclass',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
