from django import template

register = template.Library()

@register.filter(name="time")
def time(number):
  return range(number)