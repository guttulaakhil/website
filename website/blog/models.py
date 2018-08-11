from django.db import models
import datetime

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255, blank=False)
    no_posts = models.IntegerField(default=0)
    no_comments = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(blank=False)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True, blank=False)
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

class Tag(models.Model):
    name = models.CharField(max_length=255, blank=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f"{self.name}"

class Comment(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=False)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, blank=False)
    comment = models.TextField(blank=False)
    date_posted = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return f"Comment by {self.author} on {self.blog}"
    