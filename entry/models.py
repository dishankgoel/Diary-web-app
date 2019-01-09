from django.db import models
from django.utils import timezone

class diary_page(models.Model):
    date = models.DateTimeField(default = timezone.now)
    text = models.TextField()
    title = models.CharField(max_length = 200)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.title
    
class todo(models.Model):
    date_added = models.DateTimeField(default = timezone.now)
    point = models.TextField()

    def __str__(self):
        str_date = str(self.date_added)
        return str_date

    def add(self):
        self.save()


