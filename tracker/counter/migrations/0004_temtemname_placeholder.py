# Generated by Django 3.1.1 on 2020-09-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0003_temtemname'),
    ]

    operations = [
        migrations.AddField(
            model_name='temtemname',
            name='placeholder',
            field=models.CharField(default='Placeholder', max_length=200),
        ),
    ]