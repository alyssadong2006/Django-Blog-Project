from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Represents a blog post
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return str(self.title)
