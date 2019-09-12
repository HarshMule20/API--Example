from django.db import models

class language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Application(models.Model):
     city = models.CharField(max_length=200)