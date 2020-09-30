from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author', [1,2,3,4,])
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertEqual([1,2,3,4,], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author', [])
        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        
    def test_repr_multiple_posts(self):
        b1 = Blog('My Day', 'John', [1,])      
        b2 = Blog('My Day', 'Deyner', [1,2,3,4,])     
        self.assertEqual(b1.__repr__(), 'My Day by John (1 post)')
        self.assertEqual(b2.__repr__(), 'My Day by Deyner (4 posts)')
