from django.db import models


class Soogikohad(models.Model):
    nimi = models.CharField(max_length=200)
    lat = models.DecimalField(decimal_places=4, max_digits=8)
    lng = models.DecimalField(decimal_places=4, max_digits=8)
    eelroad = models.IntegerField(default=0)
    supid = models.IntegerField(default=0)
    praed = models.IntegerField(default=0)
    magustoidud = models.IntegerField(default=0)
    joogid = models.IntegerField(default=0)
    kohvilaud = models.IntegerField(default=0)
    hindajaid = models.IntegerField(default=0)




