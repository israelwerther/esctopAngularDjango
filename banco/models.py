from django.db import models

class Banco(models.Model):
    banco = models.CharField("Banco", max_length=50)
    
    def __str__(self):
        return self.banco
   
