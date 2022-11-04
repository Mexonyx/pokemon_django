from django.db import models

# Create your models here.

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    urlImage = models.CharField(max_length=500)
    type = models.CharField(max_length=50)

    def __str__(self):
        return  str(self.id) + " " + self.name + " " + self.type + "\n"