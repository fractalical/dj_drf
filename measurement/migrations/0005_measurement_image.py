# Generated by Django 4.1.7 on 2023-02-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_alter_measurement_sensor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
