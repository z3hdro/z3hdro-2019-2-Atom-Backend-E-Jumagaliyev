# Generated by Django 2.2.5 on 2019-11-06 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'Диалог', 'verbose_name_plural': 'Диалоги'},
        ),
    ]
