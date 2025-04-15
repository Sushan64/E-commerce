from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
  
  men = models.Category.objects.get(name="Men")
  clothes = models.Category.objects.get(name="Clothes")
  
  
  
  items = models.Items.objects.all()
  category_cloth = models.Items.objects.filter(category = clothes)
  category_men = models.Items.objects.filter(category = men)

  context = {
    'items': items,
    'category_cloth': category_cloth,
    'category_men': category_men,
  }
  
  return render(request, 'ecommerce/home.html', context)