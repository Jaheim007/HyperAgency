# Generated by Django 4.0.5 on 2022-06-04 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0009_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.URLField(max_length=500),
        ),
    ]
