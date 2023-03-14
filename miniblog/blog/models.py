from django.db import models
from django.contrib.auth.models import User

class Blogger(models.Model):
    """ Model representing a blog author. """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, help_text='Enter a brief description of the blogger')

    def __str__(self):
        """ String for representing the Model object. """
        return self.user.username

class BlogPost(models.Model):
    """ Model representing a blog post. """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Blogger', on_delete=models.CASCADE)
    content = models.TextField(max_length=5000, help_text='Enter the blog post content')
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ String for representing the Model object. """
        return self.title

class BlogComment(models.Model):
    """ Model representing a blog comment. """
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000, help_text='Enter the blog comment content')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ String for representing the Model object. """
        return self.comment