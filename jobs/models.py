from django.db import models

class Job(models.Model):
    title = models.CharField(default='My title',max_length=50)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    fulltext = models.TextField(default='My full text')
    show =  models.BooleanField(default=1)

    def __str__(self):
        return self.title
    

  
