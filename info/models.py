from django.db import models


# Create your models here.
class Info(models.Model):
    """"""
    name = models.CharField(max_length=30, null=False) #null чтобы не было пустое
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(null=False)
    price = models.FloatField(null=False)
    is_buy = models.BooleanField(null=False, default=False)
