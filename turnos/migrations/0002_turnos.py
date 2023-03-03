# Generated by Django 4.1.7 on 2023-03-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('disponible', models.BooleanField()),
            ],
        ),
    ]