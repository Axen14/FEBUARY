# Generated by Django 4.2.1 on 2025-02-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcoop_app', '0003_alter_loan_control_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='control_number',
            field=models.CharField(default='c20ea', max_length=5, primary_key=True, serialize=False, unique=True),
        ),
    ]
