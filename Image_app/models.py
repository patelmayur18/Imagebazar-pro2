from django.db import models

# Create your models here.
class Category(models.Model):
    title= models.CharField(max_length=200)
    discription = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Image(models.Model):
    title= models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    image = models.ImageField()
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title