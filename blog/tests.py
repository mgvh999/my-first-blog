
from django.core.urlresolvers import resolve
from django.test import TestCase
# import the HttpRequest to obtain requests for testing
from django.http import HttpRequest
# import the django render_to_string function
from django.template.loader import render_to_string
# import the home_page view
from blog.views import post_edit
from blog.models import Post
from django.contrib.auth.models import User

class PostEditTest(TestCase):

    def test_post_edit_image_post(self):
        user = User.objects.create(username="max", password="1234")
        post = Post.objects.create(author_id=user.id, title='pepe',text="pepe frog", image="test_files/pepe.jpg")
        request = HttpRequest()
        response = post_edit(request, pk=post.pk)
        self.assertIn('Image ', response.content.decode())

