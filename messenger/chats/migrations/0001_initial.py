# Generated by Django 2.2.5 on 2019-12-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_group_chat', models.BooleanField(verbose_name='Групповой чат')),
                ('topic', models.CharField(max_length=64, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Диалог',
                'verbose_name_plural': 'Диалоги',
            },
        ),
    ]
