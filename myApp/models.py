from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Train(models.Model):
    name = models.CharField(max_length=100)
    origin = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='origin_trains')
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='destination_trains')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return self.name
