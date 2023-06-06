from django.db import models

# Create your models here.

class subscribe(models.Model):
    subMail = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.subMail