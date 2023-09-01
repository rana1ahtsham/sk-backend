from django.db import models


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Nature(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Provider(models.Model):
    id = models.IntegerField(primary_key=True)
    listings_name = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    service_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    service_nature = models.ForeignKey(Nature, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
