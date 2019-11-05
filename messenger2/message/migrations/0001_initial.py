# Generated by Django 2.2.5 on 2019-11-05 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('added_at', models.DateField(verbose_name='Время добавления')),
                ('chat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chats.Chat', verbose_name='Диалог')),
            ],
        ),
    ]
