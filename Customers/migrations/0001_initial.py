# Generated by Django 4.0.5 on 2022-06-03 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dial_code', models.CharField(max_length=4)),
                ('phone', models.CharField(max_length=10)),
                ('image', models.URLField()),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user_type', models.CharField(choices=[('AD', 'admin'), ('AG', 'agent'), ('CL', 'client')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('delete_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InfoAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Biographie', models.TextField(max_length=500)),
                ('fb_link', models.URLField(blank=True, null=True)),
                ('insta_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('whatsapp_number', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('delete_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_info_agent', to='Customers.customer')),
            ],
        ),
    ]
