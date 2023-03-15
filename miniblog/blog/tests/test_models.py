from django.test import TestCase
from blog.models import Blogger, BlogPost, BlogComment
from django.contrib.auth.models import User


class BloggerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        bob = User.objects.create_user(username="Bob", password="12345")
        Blogger.objects.create(user=bob, bio="This is a bio")

    def test_user_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_bio_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field("bio").verbose_name
        self.assertEqual(field_label, "bio")

    def test_bio_max_length(self):
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field("bio").max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_user(self):
        blogger = Blogger.objects.get(id=1)
        expected_object_name = f"{blogger.user}"
        self.assertEqual(expected_object_name, str(blogger))

    def test_string_representation(self):
        blogger = Blogger.objects.get(id=1)
        self.assertEqual(str(blogger), blogger.user.username)

    def test_get_absolute_url(self):
        blogger = Blogger.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(blogger.get_absolute_url(), "/blog/blogger/1")

class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        bobUser = User.objects.create_user(username="Bob", password="12345")
        bobBlogger = Blogger.objects.create(user=bobUser, bio="This is a bio")
        BlogPost.objects.create(title="This is a title", blogger=bobBlogger, content="This is a content")

    def test_title_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_blogger_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field("blogger").verbose_name
        self.assertEqual(field_label, "blogger")

    def test_content_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field("content").verbose_name
        self.assertEqual(field_label, "content")

    def test_date_posted_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field("date_posted").verbose_name
        self.assertEqual(field_label, "date posted")

    def test_date_updated_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field("date_updated").verbose_name
        self.assertEqual(field_label, "date updated")

    def test_title_max_length(self):
        blogpost = BlogPost.objects.get(id=1)
        max_length = blogpost._meta.get_field("title").max_length
        self.assertEqual(max_length, 200)
    
    def test_content_max_length(self):
        blogpost = BlogPost.objects.get(id=1)
        max_length = blogpost._meta.get_field("content").max_length
        self.assertEqual(max_length, 5000)

    def test_object_name_is_title(self):
        blogpost = BlogPost.objects.get(id=1)
        expected_object_name = f"{blogpost.title}"
        self.assertEqual(expected_object_name, str(blogpost))

    def test_string_representation(self):
        blogpost = BlogPost.objects.get(id=1)
        self.assertEqual(str(blogpost), blogpost.title)

    def test_get_absolute_url(self):
        blogpost = BlogPost.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(blogpost.get_absolute_url(), "/blog/1")

class BlogCommentTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        bobUser = User.objects.create_user(username="Bob", password="12345")
        bobBlogger = Blogger.objects.create(user=bobUser, bio="This is a bio")
        blogPost = BlogPost.objects.create(title="This is a title", blogger=bobBlogger, content="This is a content")
        sarahUser = User.objects.create_user(username="Sarah", password="12345")
        BlogComment.objects.create(post=blogPost, commenter=bobUser, comment="This is a comment from Bob")
        BlogComment.objects.create(post=blogPost, commenter=sarahUser, comment="This is a comment from Sarah")

    def test_post_label(self):
        blogcomment = BlogComment.objects.get(id=1)
        field_label = blogcomment._meta.get_field("post").verbose_name
        self.assertEqual(field_label, "post")
        
    def test_commenter_label(self):
        blogcomment = BlogComment.objects.get(id=1)
        field_label = blogcomment._meta.get_field("commenter").verbose_name
        self.assertEqual(field_label, "commenter")

    def test_comment_label(self):
        blogcomment = BlogComment.objects.get(id=1)
        field_label = blogcomment._meta.get_field("comment").verbose_name
        self.assertEqual(field_label, "comment")

    def test_date_posted_label(self):
        blogcomment = BlogComment.objects.get(id=1)
        field_label = blogcomment._meta.get_field("date_posted").verbose_name
        self.assertEqual(field_label, "date posted")

    def test_comment_max_length(self):
        blogcomment = BlogComment.objects.get(id=1)
        max_length = blogcomment._meta.get_field("comment").max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_comment(self):
        blogcomment = BlogComment.objects.get(id=1)
        expected_object_name = f"{blogcomment.comment}"
        self.assertEqual(expected_object_name, str(blogcomment))

    def test_string_representation(self):
        blogcomment = BlogComment.objects.get(id=1)
        self.assertEqual(str(blogcomment), blogcomment.comment)

    def test_comment_help_text(self):
        blogcomment = BlogComment.objects.get(id=1)
        help_text = blogcomment._meta.get_field("comment").help_text
        self.assertEqual(help_text, "Enter comment about blog here.")