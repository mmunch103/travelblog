from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    # @permalink
    # def get_absolute_url(self):
    #     return ('view_blog_post', None, { 'slug': self.slug })
