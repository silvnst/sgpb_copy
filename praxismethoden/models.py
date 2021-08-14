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
    likes = models.ManyToManyField("User", related_name="methods_liked", blank=True)
    titel = models.CharField(max_length=255)
    desc = RichTextField(null=True, blank=True, verbose_name="Text kurz", help_text="Der hier eingegebene Kurztext, wird in der Kachelansicht angezeigt und dient zur Information und dazu, den Besucher neugierig zu machen.")
    content = RichTextField(null=True, blank=True, verbose_name="Text detail", help_text="Der Text hier ist detailierter als der Kurztext. Zum Beispiel hält dieser zusätzliche Informationen oder Beispiele.")
    file = models.FileField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField("Category", related_name="categories_method", blank=True)

    def serialize(self):
        return {
            "id": self.id,
            "likes": [user.id for user in self.likes.all()],
            "titel": self.titel,
            "desc": self.desc,
            "file": {
                "name": self.file.name,
                "url": self.file.url
            },
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "category": {
                "id": [cat.id for cat in self.category.all()],
                "name": [cat.name for cat in self.category.all()],
            }
        }

    def __str__(self):
        return f'{self.titel}, zuletzt geändert: {self.timestamp}'

PRIO_CHOICES = (
    (1,'Hoch'),
    (2, 'Mittel'),
    (3,'Tief'),
)

class Aufgaben(models.Model):
    text = models.TextField(max_length=2048)
    prio = models.PositiveSmallIntegerField(choices=PRIO_CHOICES, default=2)


class Semester(models.Model):    
    plan = RichTextField(null=True, blank=True, verbose_name="Semesterprogram", help_text="Das Semesterprogramm.")
    author = models.ForeignKey("User", blank=True, null=True, on_delete=models.SET_NULL, related_name="author")
    
    def __str__(self):
        return f'Semesterprogram von {self.author}'
