from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def home(request):
  
  category = models.Category.objects.all()
  
  items = models.Items.objects.all().order_by('-id')
  category_cloth = models.Items.objects.filter(category = category.get(name = "Clothes")).order_by('-id')
  category_men = models.Items.objects.filter(category = category.get(name = "Men")).order_by('-id')

  banners = models.Banners.objects.all()

  context = {
    'items': items,
    'banners': banners,
    'category_cloth': category_cloth,
    'category_men': category_men,
  }
  
  return render(request, 'ecommerce/home.html', context)

def product_view(request, slug):
  
  product = get_object_or_404(models.Items, slug=slug)
  review = product.review.all()
  
  score = 0
  for reviews in review:
    score = reviews.rating + score

  total = review.count()
  if total:
    avg = score / total
  else:
    avg = 0
    
  return render(request, 'ecommerce/product.html', {'product':product, 'review':review, 'avg':avg})


def login(request):
  return render(request, 'ecommerce/login.html')