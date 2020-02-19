from django.db import models
from datetime import datetime

# Create your models here.
class Logs(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    time = models.DateTimeField(default=datetime.now())