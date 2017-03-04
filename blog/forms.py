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
    image = CloudinaryJsFileField()

class PhotoUnsignedDirectForm(PostForm):
    upload_preset_name = "sample_" + hashlib.sha1(to_bytes(cloudinary.config().api_key + cloudinary.config().api_secret)).hexdigest()[0:10]
    image = CloudinaryUnsignedJsFileField(upload_preset_name)