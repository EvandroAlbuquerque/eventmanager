from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nome}-{self.email}'
