# Generated by Django 5.1.4 on 2025-01-27 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakfastofchampions', '0003_markdowncontent_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markdowncontent',
            name='image',
            field=models.ImageField(default='/static/hello.png', upload_to='breakfastofchampions/static/'),
        ),
    ]
