from django.db import models

# Create your models here.

class T_Act(models.Model):
    T_ActDist = models.DecimalField(max_digits=10,decimal_places=2)
    T_ActDuration = models.CharField(max_length=60)
    T_ActStartDate = models.CharField(max_length=30)
    T_ActAvgSpd = models.DecimalField(max_digits=10,decimal_places=2)
    T_ActCalBurn = models.PositiveIntegerField()
