from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.deletion import CASCADE

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
    desc = RichTextField(null=True, blank=True, verbose_name="Beschreibung", help_text="Der hier eingegebene Text beschreibt die Methode.")
    tipp = RichTextField(null=True, blank=True, verbose_name="Tipp", help_text="Hier noch ein Text, welcher als Tipp zur Methode angezeigt wird.")
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField("Category", related_name="categories_method", blank=True)

    def serialize(self):
        
        files = Method.objects.get(pk=self.id).method_files.all()

        return {
            "id": self.id,
            "likes": [user.id for user in self.likes.all()],
            "titel": self.titel,
            "desc": self.desc,
            "tipp": self.tipp,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "category": {
                "id": [cat.id for cat in self.category.all()],
                "name": [cat.name for cat in self.category.all()],
            } if self.category else { },
            "files": {
                "name": [f.file_name for f in files],
                "url": [f.file.url for f in files],
            } if files else { },
        }

    def __str__(self):
        return f'{self.id}: {self.titel}, zuletzt geändert: {self.timestamp}'    

class File(models.Model):
    method = models.ManyToManyField("Method", related_name="method_files", blank=True)
    file_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='raw/', storage=RawMediaCloudinaryStorage(), verbose_name="Dokument")

    def __str__(self):
        return f'{self.id}: {self.file_name}'


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
