from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Aircraft(models.Model):
    model = models.CharField(max_length=200)
    range = models.IntegerField(default=0)

    def __str__(self):
        return self.model


class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)


class Airport(models.Model):
    airport_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    longitude = models.CharField(max_length=70)
    latitude = models.CharField(max_length=70)
    timezone = models.CharField(max_length=10)

    def __str__(self):
        return self.airport_name


class Flight(models.Model):
    flight_number = models.IntegerField(default=0)
    scheduled_departure = models.DateTimeField()
    scheduled_arrivial = models.DateTimeField()
    aircraft = models.ForeignKey(Aircraft, models.SET_NULL, blank=True, null=True, related_name='+')
    airport_departure = models.ForeignKey(Airport, models.SET_NULL, blank=True, null=True, related_name='+')
    airport_arrivial = models.ForeignKey(Airport, models.SET_NULL, blank=True, null=True, related_name='+')

    def __str__(self):
        return self.flight_number
