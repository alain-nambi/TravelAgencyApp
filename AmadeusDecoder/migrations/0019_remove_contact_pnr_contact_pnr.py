# Generated by Django 4.0.6 on 2022-09-01 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0018_remove_pnr_exportstatus_pnr_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='pnr',
        ),
        migrations.AddField(
            model_name='contact',
            name='pnr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='AmadeusDecoder.pnr'),
        ),
    ]
