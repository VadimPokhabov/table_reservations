# Generated by Django 4.2 on 2024-08-18 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_alter_reservation_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.table', verbose_name='Номер стола'),
        ),
    ]
