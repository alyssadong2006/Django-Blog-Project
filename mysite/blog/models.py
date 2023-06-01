from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Represents a blog post
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True) #sets on create
    updated = models.DateTimeField(auto_now=True) #updates on each save
    #after this, use: python manage.py makemigrations  *to enable migrations*
    #after, in the blog file, there should be a migrations folder with some files in it
    
    class Meta:
        #if you want to order the posts through the 'created' category, use ['-{the category you want to use to sort}']
        ordering = ['-created']

    #use <python manage.py migrate> to apply migrations
    def __str__(self):
        return self.title
