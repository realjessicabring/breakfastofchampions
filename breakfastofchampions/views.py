from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
import markdown

from breakfastofchampions.models import MarkdownContent


def index(request):
      return render(request, 'index.html')

def blog(request):
      markdown_content = MarkdownContent.objects.all().order_by('-timestamp')
      context = {"markdown_content": markdown_content}
      return render(request, 'blog.html', context)

def markdown_content_view(request, slug):
     print(request)
     markdown_content = get_object_or_404(MarkdownContent, slug=slug)
     context = {"markdown_content": markdown_content}
# print(markdown_content.title);
     return render(
        request,
        "breakfastofchampions/markdown_content.html",
        context=context
    )