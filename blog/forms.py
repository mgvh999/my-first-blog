from django import forms
from .models import Post
from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField
from cloudinary.compat import to_bytes
import cloudinary, hashlib

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields = ('title', 'text')

class PostPhotoDirectForm(PostForm):
    image = CloudinaryJsFileField(
            attrs = { 'style': "margin-top: 30px" }, 
            options = { 
              'tags': "directly_uploaded",
              'crop': 'limit', 'width': 500, 'height': 500},
            required=False
              )

