"""code models"""
from django.db import models

class Post(models.Model):
    """represents a blog post"""
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """ordering blogs by created tag"""
        ordering = ['-created']

    def __str__(self):
        """creates title for blog post"""
        return str(self.title)
