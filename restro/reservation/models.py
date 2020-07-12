from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=30, default="your Name")
    email = models.CharField(max_length=50, default="your Email")
    phone = models.IntegerField(null=True)
    number_of_persons = models.IntegerField(null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Reservations'
