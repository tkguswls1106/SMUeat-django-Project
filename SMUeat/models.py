from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=30)
    PLACE_CATEGORY_CHOICES = (
    ('식당', '식당'),
    ('술먹기좋은식당 and 술집', '술먹기좋은식당 and 술집'),
    )
    category = models.CharField(max_length=40, choices=PLACE_CATEGORY_CHOICES)
    # password

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    point = models.IntegerField()
    menu = models.CharField(max_length=30)
    comment = models.TextField()
    # password

    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)