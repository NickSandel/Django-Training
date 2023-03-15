from django.test import TestCase
from django.urls import reverse
from blog.models import BlogPost, Blogger, BlogComment
import datetime

from django.utils import timezone
from django.contrib.auth.models import User


class BlogPostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        bob = User.objects.create_user(username="Bob", password="12345")
        bobBlogger = Blogger.objects.create(user=bob, bio="This is a bio")

        number_of_posts = 8
        for post_num in range(number_of_posts):
            BlogPost.objects.create(
                title=f"Title {post_num}",
                blogger=bobBlogger,
                content=f"Content {post_num}",
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogpost_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blogpost_list']) == 5)

    def test_lists_all_posts(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('blogs')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blogpost_list']) == 3)

    def test_blog_titles_are_displayed(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('blogpost_list' in response.context)
        self.assertTrue(len(response.context['blogpost_list']) == 5)
        for blogpost in response.context['blogpost_list']:
            self.assertTrue(blogpost.title in response.content.decode())

class BlogPostDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        bob = User.objects.create_user(username="Bob", password="12345")
        bobBlogger = Blogger.objects.create(user=bob, bio="This is a bio")

        number_of_posts = 2
        for post_num in range(number_of_posts):
            BlogPost.objects.create(
                title=f"Title {post_num}",
                blogger=bobBlogger,
                content=f"Content {post_num}",
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogpost-detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogpost-detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogpost_detail.html')

    def test_blog_title_is_displayed(self):
        response = self.client.get(reverse('blogpost-detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('blogpost' in response.context)
        self.assertTrue(response.context['blogpost'].title in response.content.decode())

class BlogCommentCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        bob = User.objects.create_user(username="Bob", password="12345")
        bobBlogger = Blogger.objects.create(user=bob, bio="This is a bio")

        number_of_posts = 2
        for post_num in range(number_of_posts):
            BlogPost.objects.create(
                title=f"Title {post_num}",
                blogger=bobBlogger,
                content=f"Content {post_num}",
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/1/create')
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogpost-create', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_logged_in_view_url_exists_at_desired_location(self):
        login = self.client.login(username='Bob', password='12345')
        response = self.client.get('/blog/1/create')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_view_url_accessible_by_name(self):
        login = self.client.login(username='Bob', password='12345')
        response = self.client.get(reverse('blogpost-create', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_view_uses_correct_template(self):
        login = self.client.login(username='Bob', password='12345')
        response = self.client.get(reverse('blogpost-create', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogcomment_form.html')

    def test_logged_in_view_creates_comment(self):
        login = self.client.login(username='Bob', password='12345')
        response = self.client.post(reverse('blogpost-create', args=[1]), {'content': 'This is a comment'})
        self.assertEqual(response.status_code, 200)
