# Generated by Django 2.2.5 on 2019-11-06 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attachment', '0002_auto_20191105_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'verbose_name': 'Прикрепление', 'verbose_name_plural': 'Прикрепления'},
        ),
    ]