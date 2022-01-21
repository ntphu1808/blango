from django import template
from django.contrib.auth.models import User
from django.utils.html import format_html
from blog.models import Post
import logging

logger=logging.getLogger(__name__)

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
  
#using format_html is the best solution, this method is the 
#composite of escapse() and mark_safe() methods
  if author.email:
    prefix=format_html('<a href="mailto:{}">', author.email)
    suffix=format_html("</a>")
  else:
    prefix=""
    suffix=""
#The first argument of the format_html is the safe string that we trust in
# and the second argument is the string we want to escape.
  if author == request_User:
    return format_html("<strong>me</strong>")
  else:
    return format_html('{}{}{}', prefix, name, suffix)


@register.simple_tag
def row(extra_classes=""): #remember that we can use the argument named as "class" because it's a python keyword
  return format_html("<div class='row {}'>", extra_classes)


@register.simple_tag
def endrow():
  return format_html("</div>")


@register.simple_tag
def col(extra_classes=""):
  return format_html("<div class='col {}'>", extra_classes)

@register.simple_tag
def endcol():
  return format_html("</div>")


@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
  posts = Post.objects.exclude(pk=post.pk).order_by("-published_at")[:5]
  logger.debug("Loaded %d recent posts for post %d", len(posts), post.pk)
  return {"title": "Recent Posts", "posts": posts}
