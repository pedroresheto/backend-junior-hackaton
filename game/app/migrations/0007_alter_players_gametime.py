# Generated by Django 4.2.7 on 2023-11-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_players_gametime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='gameTime',
            field=models.CharField(default='Без таймера', max_length=100),
        ),
    ]
