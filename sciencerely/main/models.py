from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

class BlogPage(Page):
    body = RichTextField()
    date = models.DateField("Post date")
    indexed_fields = ('body', )
    search_name = "Blog Page"

BlogPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date'),
    FieldPanel('body', classname="full"),
]

class GeneralPage(Page):
    body = RichTextField()

GeneralPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('body', classname="full"),
]