from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('code', 'Programación'),
        ('video', 'Edición Video'),
        ('music', 'Producción Musical'),
        ('english', 'Inglés Técnico'),
        ('consulting', 'Asesoría'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)  # Para videos de YouTube
    featured = models.BooleanField(default=False)  # Para el carrusel