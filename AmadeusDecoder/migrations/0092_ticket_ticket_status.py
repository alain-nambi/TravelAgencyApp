# Generated by Django 4.0.6 on 2022-10-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0091_pnrairsegments_segment_state_pnrhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_status',
            field=models.IntegerField(default=1),
        ),
    ]
