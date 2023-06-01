# Generated by Django 4.2.1 on 2023-05-24 08:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_billingstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewinstallationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_box', models.BooleanField(default=False)),
                ('no_box', models.BooleanField(default=False)),
                ('customer_cancel', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('create_at', models.DateField(default=django.utils.timezone.now)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.newinstallation')),
            ],
        ),
    ]
