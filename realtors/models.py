from django.db import models
from datetime import datetime
# blank = do optional the field

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos\%y\%m\%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    zipcode = models.BooleanField(default=False)
    description = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
