# Generated by Django 4.0.6 on 2022-10-25 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0100_merge_20221025_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_pnr',
        ),
        migrations.AddField(
            model_name='pnrhistory',
            name='agency_code_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pnrhistory',
            name='agent_username',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pnrhistory',
            name='currency_code_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pnrhistory',
            name='parent_pnr_number',
            field=models.CharField(max_length=6, null=True),
        ),
        # migrations.AddField(
        #    model_name='ticketpassengersegment',
        #    name='fare',
        #    field=models.DecimalField(decimal_places=4, default=0, max_digits=11),
        # ),
        # migrations.AddField(
        #   model_name='ticketpassengersegment',
        #    name='tax',
        #    field=models.DecimalField(decimal_places=4, default=0, max_digits=11),
        # ),
        # migrations.AddField(
        #    model_name='ticketpassengersegment',
        #    name='total',
        #    field=models.DecimalField(decimal_places=4, default=0, max_digits=11),
        # ),
        migrations.AlterField(
            model_name='pnrhistory',
            name='agency',
            field=models.ForeignKey(db_column='agency_code', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_pnrs', to='AmadeusDecoder.office', to_field='code'),
        ),
        migrations.AlterField(
            model_name='pnrhistory',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_pnrs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pnrhistory',
            name='currency',
            field=models.ForeignKey(db_column='currency_code', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_pnrs', to='AmadeusDecoder.currency', to_field='code'),
        ),
        migrations.AlterField(
            model_name='pnrhistory',
            name='parent_pnr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_children', to='AmadeusDecoder.pnr'),
        ),
        migrations.AlterField(
            model_name='pnrhistory',
            name='pnr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='histories', to='AmadeusDecoder.pnr'),
        ),
    ]
