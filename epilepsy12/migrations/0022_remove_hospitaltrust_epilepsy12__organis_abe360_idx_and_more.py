# Generated by Django 4.0.4 on 2022-07-31 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0021_alter_site_hospital_trust'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='hospitaltrust',
            name='epilepsy12__Organis_abe360_idx',
        ),
        migrations.AddIndex(
            model_name='hospitaltrust',
            index=models.Index(fields=['ParentName'], name='epilepsy12__ParentN_6c4b26_idx'),
        ),
    ]