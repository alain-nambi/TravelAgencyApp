# Generated by Django 4.0.6 on 2022-09-30 11:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0065_rename_creationdate_pnr_gds_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pnr',
            name='system_creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 11, 53, 36, 109210, tzinfo=utc)),
        ),
    ]
