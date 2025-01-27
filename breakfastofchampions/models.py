from django.db import models

class MarkdownContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(blank=True)
    image = models.ImageField(default='breakfastofchampions/static/hello.png', upload_to='assets/')
    timestamp = models.DateField(auto_now=True)
    intro = models.CharField(max_length=500, default="Nothing to see here!")
    class Meta:
        verbose_name_plural = "Markdown content"

    def __str__(self):
        return self.title