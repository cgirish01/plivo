from django.test import TestCase
from .models import Message

class MessageModelTestCase(TestCase):
    def setUp(self):
        self.message = Message.objects.create(
            src='+1234567890',
            dst='+0987654321',
            text='Hello, World!'
        )

    def test_message_str(self):
        self.assertEqual(str(self.message), 'Hello, World!')

    def test_message_fields(self):
        self.assertEqual(self.message.src, '+1234567890')
        self.assertEqual(self.message.dst, '+0987654321')
        self.assertEqual(self.message.text, 'Hello, World!')