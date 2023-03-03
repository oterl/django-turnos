# Generated by Django 4.1.7 on 2023-03-03 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0002_turnos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnos',
            name='disponible',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turnos.usuarios'),
        ),
    ]