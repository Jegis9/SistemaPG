# Generated by Django 5.1 on 2024-08-29 20:37

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0002_insumos_cantidadtomada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insumos',
            name='cantidadTomada',
        ),
        migrations.CreateModel(
            name='InsumoLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadTomada', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fecha_hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='Administrativo.insumos')),
            ],
        ),
    ]
