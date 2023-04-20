# Generated by Django 4.0.7 on 2022-10-19 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AmadeusDecoder', '0095_comment_response_model_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='document_number',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='document_parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AmadeusDecoder.notification', to_field='document_number'),
        ),
    ]
