from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import  get_user_model






class Booking(models.Model):
    table_no = models.CharField(max_length=10)
    order = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, default="")
    add = models.CharField(max_length=50, default="")
    
    

    def __str__(self):
        return f"{self.customer}"
