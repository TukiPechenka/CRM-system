# Generated by Django 5.0.7 on 2024-08-04 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmsystem', '0002_ad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
