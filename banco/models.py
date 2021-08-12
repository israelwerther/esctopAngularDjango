from django.db import models

class Banco(models.Model):
    banco = models.CharField("Banco", max_length=50)
    
   
