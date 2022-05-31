from django.db import models

class Catergory(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

print_sizes = (
    ("A4", "A4"),
    ("A3", "A3"),
    ("card", "card"),
)

class Product(models.Model):
    catergory = models.ForeignKey('Catergory', null = True, blank = True, on_delete = models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    print_sizes = models.CharField(max_length=4, choices=print_sizes, default="A4")

    def __str__(self):
        return self.name
