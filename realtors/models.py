from django.db import models
from datetime import datetime
# blank = do optional the field

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos\%y\%m\%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    
# Method that gives a name instead of a object, in the admin Realtor section 
    def __str__(self):
        return self.name
