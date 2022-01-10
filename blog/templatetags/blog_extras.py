from django import template
from django.contrib.auth.models import User
from django.utils.html import format_html

register=template.Library()

@register.filter()

def author_details(author, request_User=None):
  if not isinstance(author, User):
          # return empty string as safe default
    return ""

  if author.first_name and author.last_name:
    name = f"{author.first_name} {author.last_name}"
  else:
    name = f"{author.username}"
  
  if author.email:
    prefix=format_html('<a href="mailto:{}">', author.email)
    suffix=format_html("</a>")
  else:
    prefix=""
    suffix=""

  if author == request_User:
    return format_html("<strong>me</strong>")
  else:
    return format_html('{}{}{}', prefix, name, suffix)