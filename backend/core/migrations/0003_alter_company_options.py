# Generated by Django 4.2.4 on 2023-08-29 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_attendance_bankinginfo_candidate_candidatekyc_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
    ]