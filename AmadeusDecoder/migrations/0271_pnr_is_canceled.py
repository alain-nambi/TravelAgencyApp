# Generated by Django 3.2.15 on 2024-02-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0270_alter_othersfee_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pnr',
            name='is_canceled',
            field=models.BooleanField(default=0),
        ),
    ]
