# Generated by Django 5.1 on 2024-10-01 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EPP', '0004_estadoepp_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadoepp',
            name='estado',
            field=models.CharField(default='malo', max_length=100),
        ),
    ]
