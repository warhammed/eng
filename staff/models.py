from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=75)
    local_phone_number = models.IntegerField()
    position = models.CharField(max_length=150)
    room_location = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "کارکنان"
        verbose_name_plural = "کارکنان"

    def __str__(self):
        return self.name
