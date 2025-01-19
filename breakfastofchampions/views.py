from django.http import HttpResponse
from django.shortcuts import render
import markdown

from breakfastofchampions.models import MarkdownContent


def index(request):
      return render(request, 'index.html')

def blog(request):
      context = {
            "blogs_array" : [
                  [{"img_link": "static/hello.png", "md_link":"hello.md"}, {}],
                  [{}, {}]
            ]
            }
      return render(request, 'blog.html', context)


def markdown_content_view(request):
    markdown_content = MarkdownContent.objects.first()
    context = {"markdown_content": markdown_content}
    return render(
        request,
        "breakfastofchampions/markdown_content.html",
        context=context
    )


def markdown_content_view(request):
    md = markdown.Markdown(extensions=["fenced_code"])
    markdown_content = MarkdownContent.objects.first()
    markdown_content.content = md.convert(markdown_content.content)
    context = {"markdown_content": markdown_content}
    return render(
        request,
        "breakfastofchampions/markdown_content.html",
        context=context
    )