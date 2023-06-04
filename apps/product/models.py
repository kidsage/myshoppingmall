from django.db import models
from core.models import BaseModel

# Create your models here.
class Product(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name