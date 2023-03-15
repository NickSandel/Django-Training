from django.contrib import admin
from .models import BlogPost, Blogger, BlogComment

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Blogger)
admin.site.register(BlogComment)