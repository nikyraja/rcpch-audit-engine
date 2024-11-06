# Generated by Django 5.1.2 on 2024-10-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("epilepsy12", "0040_banner"),
    ]

    operations = [
        migrations.AddField(
            model_name="assessment",
            name="consultant_paediatrician_input_achieved",
            field=models.BooleanField(
                blank=True,
                default=None,
                help_text={
                    "label": "Has the child been seen by a paediatrician with expertise in epilepsy by the end of the audit year?",
                    "reference": "Children with epilepsy should be seen by a paediatrician with expertise in epilepsy. If the child has been seen by a paediatrician with expertise in epilepsy by the end of the audit year, please select this option to enter the date seen.",
                },
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="assessment",
            name="epilepsy_specialist_nurse_input_achieved",
            field=models.BooleanField(
                blank=True,
                default=None,
                help_text={
                    "label": "Has the child been seen by an epilepsy nurse specialist by the end of the audit year?",
                    "reference": "Children with epilepsy should be seen by an epilepsy nurse specialist. If the child has been seen by an epilepsy nurse specialist by the end of the audit year, please select this option to enter the date seen.",
                },
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="assessment",
            name="paediatric_neurologist_input_achieved",
            field=models.BooleanField(
                blank=True,
                default=None,
                help_text={
                    "label": "Has the child been seen by a paediatric neurologist by the end of the audit year?",
                    "reference": "Children with epilepsy should be seen by a paediatric neurologist. If the child has been seen by a paediatric neurologist by the end of the audit year, please select this option to enter the date seen.",
                },
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="historicalassessment",
            name="consultant_paediatrician_input_achieved",
            field=models.BooleanField(
                blank=True,
                default=None,
                help_text={
                    "label": "Has the child been seen by a paediatrician with expertise in epilepsy by the end of the audit year?",
                    "reference": "Children with epilepsy should be seen by a paediatrician with expertise in epilepsy. If the child has been seen by a paediatrician with expertise in epilepsy by the end of the audit year, please select this option to enter the date seen.",
                },
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="historicalassessment",
            name="epilepsy_specialist_nurse_input_achieved",
            field=models.BooleanField(
                blank=True,
                default=None,
                help_text={
                    "label": "Has the child been seen by an epilepsy nurse specialist by the end of the audit year?",
                    "reference": "Children with epilepsy should be seen by an epilepsy nurse specialist. If the child has been seen by an epilepsy nurse specialist by the end of the audit year, please select this option to enter the date seen.",
                },
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="historicalassessment",
            name="paediatric_neurologist_input_achieved",
            field=models.BooleanField(
                blank=True,
                default=None,
                help_text={
                    "label": "Has the child been seen by a paediatric neurologist by the end of the audit year?",
                    "reference": "Children with epilepsy should be seen by a paediatric neurologist. If the child has been seen by a paediatric neurologist by the end of the audit year, please select this option to enter the date seen.",
                },
                null=True,
            ),
        ),
    ]
