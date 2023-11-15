from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='imgs')
    desc = models.TextField()

    # for name in admin panel, other than object
    def __str__(self):
        return self.name


class Team(models.Model):
    crew = models.CharField(max_length=50)
    c_img = models.ImageField(upload_to='imgs')
    c_desc = models.TextField()

    def __str__(self):
        return self.crew
