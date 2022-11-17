from django.db import models


class CountLang(models.Model):
    country = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.country


