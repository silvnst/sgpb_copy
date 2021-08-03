from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=255)

    def lower(self):
        return self.name.lower()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "name_lower": self.name.lower(),
        }

    def __str__(self):
        return f'Kategorie {self.id}: {self.name}'

class Method(models.Model):
    author = models.ForeignKey("User", null=True, on_delete=models.SET_NULL, related_name="author")
    likes = models.ManyToManyField("User", related_name="methods_liked", blank=True)
    titel = models.CharField(max_length=255)
    desc = RichTextField(null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField("Category", related_name="categories_method", blank=True)

    def serialize(self):
        return {
            "id": self.id,
            "author": self.author.id,
            "likes": [user.id for user in self.likes.all()],
            "titel": self.titel,
            "desc": self.desc,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "category": [cat.name for cat in self.category.all()]
        }

    def __str__(self):
        return f'{self.titel} von {self.author}, zuletzt geändert: {self.timestamp}'
