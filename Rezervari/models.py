from django.db import models

class Rezervare(models.Model):
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    email_sau_telefon = models.CharField(max_length=100)
    data = models.DateField()
    ora = models.TimeField()

    def __str__(self):
        return f"{self.nume} {self.prenume} - {self.data} {self.ora}"
    
    