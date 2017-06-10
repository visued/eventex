from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Victor Sued', cpf='40182589846',
                    email='visued@gmail.com', phone='16-99342-3942')
        self.email = mail.outbox[0]
        

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, .self.email.subject)


    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, .self.email.from_email)


    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'visued@gmail.com']
        self.assertEqual(expect, .self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Victor Sued',
            '40182689846',
            'visued@gmail.com',
            '16-99342-3942'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)