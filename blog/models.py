from django.db import models

# Create your models here.
class Blog(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

