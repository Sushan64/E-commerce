from django.db import models
from django.utils.text import slugify
from django.conf import settings

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100, unique= True)
  parents = models.ForeignKey('Category', on_delete= models.CASCADE, null = True, blank = True, related_name ="SubCategory")

  def __str__(self):
    return self.name

#Function for auto generator slug
def generate_slug(instance):
  base_slug = slugify(instance.name)
  slug = base_slug
  num = 1
  while Items.objects.filter(slug=slug).exists():
    slug = f"{base_slug}-{num}"
    num+=1
  return slug

class Items(models.Model):
  name = models.CharField(max_length = 200)
  image = models.ImageField(upload_to="Pictures/")
  description= models.TextField()
  price = models.DecimalField(max_digits=30, decimal_places =2)
  slug = models.SlugField(max_length=200, blank = True, unique=True, null = True)
  category = models.ManyToManyField(Category, related_name="Items")
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = generate_slug(self)
    super().save(*args, **kwargs)
      
    
  def __str__(self):
    return self.name


class Review(models.Model):
  scores = [
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★'),
  ]
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  product = models.ForeignKey(Items, on_delete=models.CASCADE)
  rating = models.IntegerField(choices=scores)
  title = models.CharField(max_length = 100)
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user} - {self.product} - Ratings"