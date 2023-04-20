# Generated by Django 4.0.6 on 2022-08-29 11:59

import AmadeusDecoder.models.BaseModel
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0005_office_pnr_agent_user_office'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=4, default=0, max_digits=11)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('state', models.CharField(max_length=200, null=True)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AmadeusDecoder.ticket')),
            ],
            options={
                'db_table': 't_payment',
            },
            bases=(models.Model, AmadeusDecoder.models.BaseModel.BaseModel),
        ),
    ]
