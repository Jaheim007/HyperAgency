# Generated by Django 4.0.5 on 2022-06-04 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0006_slider_address_number1_slider_address_number2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='address3',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='address_number1',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='address_number2',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='address_number3',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='title3',
        ),
        migrations.AddField(
            model_name='slider',
            name='address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slider',
            name='address_number',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slider',
            name='image',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
