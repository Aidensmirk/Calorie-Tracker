from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

class FoodItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.name} - {self.calories} cal"
