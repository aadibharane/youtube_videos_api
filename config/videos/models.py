from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateTimeField()
    thumbnail_url = models.URLField()

    class Meta:
        indexes = [
            models.Index(fields=['published_at']),
            models.Index(fields=['title']),
            models.Index(fields=['description']),
        ]

    def __str__(self):
        return self.title
