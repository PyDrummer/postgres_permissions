from django.db import models
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Blog

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        testblog = Blog.objects.create(
            author = testuser1,
            blog = 'Mazda',
            body = 'Miata',
            created_at = models.DateTimeField(auto_now_add=True)
        )
        testblog.save()

    def test_blog_content(self):
        blog = Blog.objects.get(id=1)
        actual_author = str(blog.author)
        actual_blog = str(blog.blog)
        actual_body = str(blog.body)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_blog, 'Mazda')
        self.assertEqual(actual_body, 'Miata')