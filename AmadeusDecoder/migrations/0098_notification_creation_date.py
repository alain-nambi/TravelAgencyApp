# Generated by Django 4.0.7 on 2022-10-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0097_notification_message_charfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
