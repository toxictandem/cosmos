from django.db import models

class Db(models.Model):
    id = models.IntegerField(primary_key=True)
    length = models.IntegerField()
    need = models.IntegerField()

class Result(models.Model):
    id = models.IntegerField(primary_key=True)
    days = models.IntegerField()
    resources = models.IntegerField()
    onShip = models.IntegerField()
    sh = models.IntegerField()