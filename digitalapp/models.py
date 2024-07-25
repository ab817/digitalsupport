# blog/models.py

from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"

class PortalSetting(models.Model):
    show_popup = models.BooleanField(default=True)
    popup_image = models.ImageField(upload_to='popup_images/', blank=True, null=True)
    #show_image = models.BooleanField(default=True)

    def __str__(self):
        return "Portal Settings"

class Feedback(models.Model):
    feedback_text = models.TextField()
    questioned_by = models.CharField(max_length=100)
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback by {self.questioned_by} on {self.submitted_on}'