from django.db import models
from django.conf import settings
from tool.models import Item
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Cart(models.Model):
  item = models.ForeignKey(
      Item, on_delete=models.CASCADE, related_name='cart'
  )
  user = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name='cart'
  )
  amount = models.IntegerField(null=True)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()
