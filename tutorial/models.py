from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=100),
    category = models.CharField(max_length=50),
    description = models.TextField(),
    price = models.IntegerField(max_length=10),
