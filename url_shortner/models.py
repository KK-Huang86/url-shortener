from django.db import models

# Create your models here.
class Url(models.Model):
  original_url=models.URLField()
  short_url=models.CharField(max_length=20)
  created_time=models.DateTimeField(auto_now_add=True)
  is_active=models.BooleanField(default=True)