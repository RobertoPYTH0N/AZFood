from django.db import models

# Create your models here.

class categorie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def get_absolute_url(self):
        return f"/meniu/categorie/{self.slug}"
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categorii'


class Reteta(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    category = models.ForeignKey(categorie, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available  = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to="imaginiproduse", null=True, blank=True)

    def get_absolute_url(self):
        return f"meniu/reteta/{self.slug}"

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Retete'