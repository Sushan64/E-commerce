from django import template

register = template.Library()

@register.filter(name="time")
def time(number):
  if type(number) == float:
    number = int(number)
  return range(number)