# Generated by Django 3.1.1 on 2020-09-28 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0003_auto_20200928_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counternumber',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='species', to='counter.speciesmodel'),
        ),
    ]
