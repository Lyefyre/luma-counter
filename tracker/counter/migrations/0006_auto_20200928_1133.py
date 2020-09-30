# Generated by Django 3.1.1 on 2020-09-28 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0005_auto_20200928_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='speciesmodel',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='counternumber',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CounterNumber', to='counter.speciesmodel'),
        ),
    ]
