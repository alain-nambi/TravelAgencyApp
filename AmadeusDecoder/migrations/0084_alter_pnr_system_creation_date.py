# Generated by Django 4.0.6 on 2022-10-07 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0083_alter_pnr_system_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pnr',
            name='system_creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 7, 11, 49, 19, 875066)),
        ),
    ]
