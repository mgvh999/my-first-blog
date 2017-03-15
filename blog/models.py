from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField
from django.core.urlresolvers import reverse
import json
from django.core.serializers.json import DjangoJSONEncoder
class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    url = models.URLField(null=True, blank=True)
    image = CloudinaryField('image', blank=True, null=True)
    video_url = models.URLField(null=True, blank=True)
    
    tags = TaggableManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()



    def __str__(self):#dunder = "double underscore"
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',
                        args=[self.pk])




