from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    STATUS_CHOICES = (
        ('d' , 'Draft') , 
        ('p' , 'Published')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    #image = models.imagefields()
    pubdate = models.DateTimeField(default = timezone.now)
    year = models.IntegerField ()
    author = models.CharField(max_length=100)
    pagenum = models.IntegerField ()
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices = STATUS_CHOICES)


    # author = models.ForeignKey(
    #         'auth.User',
    #         on_delete=models.CASCADE,
    # )



   

    def __str__(self):
        return self.title