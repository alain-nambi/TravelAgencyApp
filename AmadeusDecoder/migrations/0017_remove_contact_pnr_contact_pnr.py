# Generated by Django 4.0.6 on 2022-08-31 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0016_alter_pnr_agent_alter_pnr_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='pnr',
        ),
        migrations.AddField(
            model_name='contact',
            name='pnr',
            field=models.ManyToManyField(to='AmadeusDecoder.pnr'),
        ),
    ]
