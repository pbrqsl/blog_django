from django.db import models
from django.db.models.query import QuerySet


class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        from blog.models import Post
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
    
# class PublishedManager(models.Manager):
#     def get_queryset(self) -> QuerySet:
#         from blog.models import Post
#         return super().get_queryset().filter(status='blog.models.Post.Status.PUBLISHED')
    