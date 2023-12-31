# Generated by Django 4.2.7 on 2023-11-12 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_players_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='players',
            old_name='record',
            new_name='turns',
        ),
        migrations.AddField(
            model_name='players',
            name='fieldSize',
            field=models.PositiveSmallIntegerField(choices=[(16, '4x4'), (20, '5x5'), (36, '6x6')], null=True),
        ),
        migrations.AddField(
            model_name='players',
            name='gameTime',
            field=models.CharField(default='Без таймера'),
        ),
    ]
