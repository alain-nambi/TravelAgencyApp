# Generated by Django 4.0.6 on 2022-08-30 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0011_alter_currencyrate_currency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_password',
            new_name='password',
        ),
    ]
