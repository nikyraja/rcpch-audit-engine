# Generated by Django 4.0 on 2022-04-24 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='lead_hospital',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lead_hospital', to='epilepsy12.hospitaltrust'),
        ),
    ]
