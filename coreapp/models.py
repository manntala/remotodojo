from django.db import models
from account.models import Account

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    published = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

