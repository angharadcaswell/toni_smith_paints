from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
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

class Size(models.Model):
    name = models.CharField(max_length=4, choices=print_sizes, default="A4")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('Category', null = True, blank = True, on_delete = models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    sizes = models.ManyToManyField(Size)

    def __str__(self):
        return self.name