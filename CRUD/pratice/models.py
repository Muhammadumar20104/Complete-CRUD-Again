from django.db import models

class Details(models.Model):
    F_Name = models.CharField(max_length=15)
    L_Name = models.CharField(max_length=15)
    def __str__(self):
        return self.F_Name