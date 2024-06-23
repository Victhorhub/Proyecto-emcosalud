# Generated by Django 5.0.6 on 2024-06-23 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='nameState',
            field=models.CharField(max_length=200, verbose_name='Nombre del estado'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCity', models.CharField(max_length=200, verbose_name='Nombre de la ciudad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.state')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'ordering': ['-created'],
            },
        ),
    ]
