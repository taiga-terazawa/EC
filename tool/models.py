from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
  name = models.CharField(max_length=200)
  price = models.IntegerField()
  image = models.ImageField(upload_to='images', blank=True, null=True)
  status = models.IntegerField()
  category = models.CharField(max_length=200)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()


def __str__(self):
  return self.name


class ItemStock(models.Model):
  item = models.ForeignKey(
      Item, on_delete=models.CASCADE, related_name='item_stocks'
  )
  stock = models.IntegerField()
  created_date = models.DateTimeField(default=timezone.now)
