from django.contrib import admin
from blog.models import Tag, Post, Comment, AuthorProfile
# Register your models here.
# This PostAdmin class used for define the slug field will be automatically updated
# when the title field changes.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug": ("title",)}

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(AuthorProfile)
