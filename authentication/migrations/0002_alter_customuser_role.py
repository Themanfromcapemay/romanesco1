# Generated by Django 4.1.7 on 2023-07-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('Technical Admin', 'Technical Admin'), ('Field Technician', 'Field Technician')], max_length=20, null=True),
        ),
    ]
