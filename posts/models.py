from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class post(models.Model):
    title = models.CharField(max_length= 100)
    content = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    image = models.ImageField(null = True)
    
    def __self__(self):
        return self.title + ' | ' + self.author
    def get_absolute_url(self):
        return reverse('Article', kwargs={'pk': self.pk})
    

    
    



