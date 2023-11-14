from django.db import models

# Create your models here.


class Players(models.Model):
    SIZE_CHOICES = (
        (16, '4x4'),
        (20, '5x5'),
        (36, '6x6')
    )

    name = models.CharField(max_length=40, default='Анонимный пользователь')
    turns = models.IntegerField(default=0)
    fieldSize = models.PositiveSmallIntegerField(choices=SIZE_CHOICES, default=16)
    gameTime = models.CharField(max_length=100, default='Без таймера')


    def __str__(self):
        return f'{self.name} :  {self.turns} turns, {self.fieldSize}, {self.gameTime}'