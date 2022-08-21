# Generated by Django 4.0.4 on 2022-08-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0047_alter_desscribe_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auditprogress',
            old_name='investigation_management_complete',
            new_name='investigation_complete',
        ),
        migrations.AddField(
            model_name='auditprogress',
            name='management_complete',
            field=models.BooleanField(default=False, null=True),
        ),
    ]