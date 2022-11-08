# Generated by Django 4.1.2 on 2022-10-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0022_alter_antiepilepsymedicine_antiepilepsy_medicine_risk_discussed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antiepilepsymedicine',
            name='antiepilepsy_medicine_type',
        ),
        migrations.AddField(
            model_name='antiepilepsymedicine',
            name='medicine_id',
            field=models.IntegerField(blank=True, default=None, help_text={'label': 'Medicine ID', 'reference': 'Please enter the medicine.'}, null=True),
        ),
        migrations.AddField(
            model_name='antiepilepsymedicine',
            name='medicine_name',
            field=models.CharField(blank=True, default=None, help_text={'label': 'Medicine name', 'reference': 'Please enter the medicine name.'}, max_length=200, null=True),
        ),
    ]