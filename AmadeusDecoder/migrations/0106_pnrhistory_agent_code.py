# Generated by Django 4.0.6 on 2022-10-27 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0105_pnrairsegments_other_segment_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pnrhistory',
            name='agent_code',
            field=models.CharField(default='', max_length=10),
        ),
    ]
