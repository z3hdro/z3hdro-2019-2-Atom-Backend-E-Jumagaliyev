# Generated by Django 2.2.5 on 2019-11-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default='empty', max_length=250, verbose_name='биография'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(max_length=32, null=True, verbose_name='аватар'),
        ),
    ]
