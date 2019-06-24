from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from first.models import blog

User = get_user_model
class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        user = User(username='testcfeuser', email='test@test.com')
        user.set_password("somerandompasswd")
        blog_post = blog.objects.create(user=user,
                                        title='New one',
                                        content='fsdfgfgd#322r')
        def test_single_user(self):
            user_count = User.objects.count()
            self.assertEqual(user_count, 1)

        def test_single_post(self):
            post = blog.objects.count()
            self.assertEqual(post, 1)   