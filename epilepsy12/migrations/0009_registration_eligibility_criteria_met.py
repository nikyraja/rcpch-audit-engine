# Generated by Django 4.0.4 on 2022-07-16 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0008_alter_case_ethnicity_alter_case_locked_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='eligibility_criteria_met',
            field=models.BooleanField(default=None, null=True),
        ),
    ]