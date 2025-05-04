from django.db import models
from django.utils.text import slugify

class Artist(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Hit(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title_url = models.SlugField(unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        title_url = slugify(self.title)
        counter = 0
        while Hit.objects.filter(title_url=title_url).exists():
            counter += 1
            title_url = f"{title_url}-{counter}"
        self.title_url = title_url
        super().save(*args, **kwargs)
