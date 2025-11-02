from datetime import datetime, timezone, tzinfo
from django.db import models
import pytz

class MarkdownContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(blank=True)
    blog_header_image = models.ImageField(default='breakfastofchampions/static/blog_filler.png',upload_to='assets/')
    image = models.ImageField(default='breakfastofchampions/static/hello.png', upload_to='assets/')
    eastern_tz = pytz.timezone('US/Eastern') 
    timestamp = models.DateField(default=datetime.now(eastern_tz))
    intro = models.CharField(max_length=500, default="Nothing to see here!")
    class Meta:
        verbose_name_plural = "Markdown content"

    def __str__(self):
        return self.title