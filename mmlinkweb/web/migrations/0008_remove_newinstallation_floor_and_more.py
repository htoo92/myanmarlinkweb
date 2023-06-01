# Generated by Django 4.2.1 on 2023-05-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_remove_complain_floor_remove_complain_house_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newinstallation',
            name='floor',
        ),
        migrations.RemoveField(
            model_name='newinstallation',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='newinstallation',
            name='latlong',
        ),
        migrations.RemoveField(
            model_name='newinstallation',
            name='street',
        ),
        migrations.RemoveField(
            model_name='newinstallation',
            name='township',
        ),
        migrations.RemoveField(
            model_name='newinstallation',
            name='ward',
        ),
        migrations.AddField(
            model_name='newinstallation',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
