# Generated by Django 4.0.6 on 2022-10-03 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0070_pnr_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pnr',
            name='system_creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 3, 11, 33, 22, 91717)),
        ),
    ]
