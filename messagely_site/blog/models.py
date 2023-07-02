"""
This is the model.py for the messagely site
"""
from django.conf import settings
from django.db import models

class Topic(models.Model):
    """
    Represents a topic
    """
    name = models.CharField(
        max_length = 50,
        unique= True
    )
    slug = models.SlugField(unique = True)
    def __str__(self):
        return str(self.name)
    class Meta:
        """
        ordering by name
        """
        ordering = ['name']

class Post(models.Model):
    """
    Represents a blog post
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(
        null=False,
        unique_for_date='published',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='blog_posts',
        null=False,
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
    )
    content = models.TextField()
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    topics = models.ManyToManyField(
        Topic,
        related_name = 'blog_posts'
    )

    class Meta:
        """
        ordering method
        """
        ordering = ['-created']

    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    """
    Represents a comment
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Unapproved'),
        (PUBLISHED, 'Approved')
    ]
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='comments',
        null=True,
    )
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'comments',
        null = True
    )

    email = models.EmailField(blank = False)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "Approved" to make this post publicly visible',
    )
    published = models.DateTimeField(auto_now_add=True)
    comment_text = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text[:50]
        #pylint shows this is unsubscriptable, but it is?
