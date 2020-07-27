from django.db import models
from category.models import Category
from django.db.models.signals import pre_save
from Portfolio.helpers import unique_slug_generator, html_from_md
# Create your models here.


class Blog(models.Model):
    title = models.CharField(
        unique=True, 
        max_length=255, 
        help_text="Enter Title", 
        blank=False
    )
    content = models.TextField(verbose_name="Content", max_length=5000)
    parsed_content = models.TextField(max_length=5000, blank=True, null=True)
    tags = models.CharField(max_length=255, help_text="Enter comma seperated String", null=True)
    highlights = models.TextField(max_length=255, help_text="Enter Phrase to be highlighted in Blog Post", null=True)
    category = models.ForeignKey(to=Category, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    image = models.ImageField(
        blank=True,
        help_text="Use Image for Im-powring your Blog"
    )
    priority = models.IntegerField(max_length=10, default=1)
    similar_post = models.ManyToManyField('self',null=True,blank=True)
    creation_time = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return self.title


class Comments(models.Model):
    message = models.TextField(max_length=160)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=45)
    creation_time = models.DateTimeField(auto_now_add=True, editable=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)





def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

def html_generator(sender, instance, *args, **kwargs):
    if not instance.parsed_content:
        instance.parsed_content = html_from_md(instance)

pre_save.connect(slug_generator, sender=Blog)
pre_save.connect(html_generator, sender=Blog)