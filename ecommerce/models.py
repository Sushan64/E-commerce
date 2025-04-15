from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100)
  parents = models.ForeignKey('Category', on_delete= models.CASCADE, null = True, blank = True, related_name ="SubCategory")

  def __str__(self):
    return self.name

class Items(models.Model):
  name = models.CharField(max_length = 200)
  image = models.ImageField(upload_to="Pictures/")
  description= models.TextField()
  price = models.DecimalField(max_digits=30, decimal_places =3)
  category = models.ManyToManyField(Category, related_name="Items")
  

  def __str__(self):
    return self.name
