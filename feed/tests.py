from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Posts, Comments

class BlogModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Posts.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user,
            tag='tech'
        )
    
    def test_post_creation(self):
        """Post model saves correctly"""
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(str(self.post), 'Test Post')
    
    def test_comment_creation(self):
        """Comment model saves and relates to post"""
        comment = Comments.objects.create(
            text='Nice post!',
            u_name=self.user,
            posts=self.post
        )
        self.assertEqual(comment.posts.title, 'Test Post')
        self.assertEqual(str(comment), 'Nice post!')

class BlogViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        Posts.objects.create(title='Hello', content='World', author=self.user, tag='tech')
    
    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello')
    
    def test_post_detail_page(self):
        post = Posts.objects.first()
        response = self.client.get(f'/post_detail/{post.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'World')
    
    def test_login_required_for_new_post(self):
        response = self.client.get('/new_posts/')
        # Should redirect to login
        self.assertEqual(response.status_code, 302)