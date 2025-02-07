# Generated by Django 5.0.6 on 2024-05-30 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('instrument_type', models.CharField(choices=[('I1', 'Instrument1'), ('I2', 'Instrument2'), ('I3', 'Instrument3')], max_length=10)),
            ],
        ),
    ]
