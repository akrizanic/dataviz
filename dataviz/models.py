from django.db import models

class Temps(models.Model):
    date = models.DateField()
    temp1 = models.DecimalField(max_digits = 5, decimal_places = 1)
    temp2 = models.DecimalField(max_digits = 5, decimal_places = 1)
    temp3 = models.DecimalField(max_digits = 5, decimal_places = 1)
    temp4 = models.DecimalField(max_digits = 5, decimal_places = 1)
