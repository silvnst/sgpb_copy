from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.base import Model
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
    files = models.ManyToManyField('File', related_name="method_files", blank=True)


    def serialize(self):
        
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
                "name": [f.file_name for f in self.files.all()],
                "url": [f.file.url for f in self.files.all()],
            } if self.files else { },
        }

    def __str__(self):
        return f'{self.id}: {self.titel}, zuletzt geändert: {self.timestamp}'    

class File(models.Model):
    file_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='raw/', storage=RawMediaCloudinaryStorage(), verbose_name="Dokument")

    def __str__(self):
        return f'{self.id}: {self.file_name}'

class Course(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='courses_created',
        on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)  
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(User, related_name="students", blank=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title

MODULE_KINDS = (
    (1, 'Meilenstein'),
    (2, 'Prüfungsleistung')
)

class Module(models.Model):
    course = models.ForeignKey(
        Course,
        related_name='modules',
        on_delete=CASCADE
    )
    module_kind = models.PositiveSmallIntegerField(choices=MODULE_KINDS, default=1, verbose_name="Art des Elements")
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=510)
    desc = RichTextField(null=True, blank=True, verbose_name="Zusammenfassung", help_text="Der hier eingegebene Text beschreibt die kurz das wichtigste zum Meilenstein.")
    tipp = RichTextField(null=True, blank=True, verbose_name="Tipp", help_text="Hier noch ein Text, welcher als Tipp zur Methode angezeigt wird.")
    files = models.ManyToManyField('File', related_name="module_files", blank=True)


    def __str__(self):
        return self.title

PRIO_CHOICES = (
    (1,'Hoch'),
    (2, 'Mittel'),
    (3,'Tief'),
)
