# Generated by Django 2.2.5 on 2019-11-13 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191113_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(default='None', max_length=32, null=True, verbose_name='аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(default='empty', max_length=250, verbose_name='биография'),
        ),
    ]