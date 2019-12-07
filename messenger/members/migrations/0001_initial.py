# Generated by Django 2.2.5 on 2019-12-04 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_messages', models.TextField(verbose_name='Новые сообщения')),
                ('chat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chats.Chat', verbose_name='Диалог')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участиники',
            },
        ),
    ]
