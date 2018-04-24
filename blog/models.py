from django.db import models
from datetime import date
from datetime import time
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.pub_date}...{self.title}'

    def summary(self):
        texti = self.body[:100]
        if len(texti)== 100:
            texti = texti + ' ...'

        return texti

    def pub_date_pretty(self):
        return self.pub_date.strftime('%A, %Y-%b-%e, %H:%M')