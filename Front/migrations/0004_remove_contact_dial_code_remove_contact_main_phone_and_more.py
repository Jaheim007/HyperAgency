# Generated by Django 4.0.5 on 2022-06-04 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0003_rename_title_siteinfo_title1_siteinfo_title2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='dial_code',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='main_phone',
        ),
        migrations.AlterField(
            model_name='contact',
            name='site_contact',
            field=models.CharField(max_length=20),
        ),
    ]
