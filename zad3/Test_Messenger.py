import unittest
from unittest.mock import *
from Messenger import Messenger


class TestMessenger(unittest.TestCase):

    def setUp(self):
        self.temp = Messenger()

    def test_send(self):
        self.temp.template = MagicMock()
        self.temp.mail = MagicMock()
        self.temp.template.message = MagicMock(return_value='Hi')
        self.temp.mail.send = MagicMock(return_value=True)
        self.assertTrue(self.temp.send('Client', 'Hi'))

    def test_send_2(self):
        self.temp.template = MagicMock()
        self.temp.mail = MagicMock()
        self.temp.template.message = MagicMock(return_value='Hi1')
        self.temp.mail.send = MagicMock(return_value=True)
        self.assertTrue(self.temp.send('Client1', 'Hi1'))

    def test_send_assert_False(self):
        self.temp.template = MagicMock()
        self.temp.mail = MagicMock()
        self.temp.template.message = MagicMock(return_value='Hi')
        self.temp.mail.send = MagicMock(return_value=False)
        self.assertFalse(self.temp.send('Client', 'Hi'))

    def test_send_wrong_client_int(self):
        self.temp.template = MagicMock()
        self.temp.mail = MagicMock()
        self.temp.template.message = MagicMock(return_value='Hi')
        self.temp.mail.send = MagicMock(side_effect=TypeError("Not a valid client"))
        self.assertRaises(TypeError, self.temp.send, 23, 'Hi')

    def test_send_wrong_client_None(self):
        self.temp.template = MagicMock()
        self.temp.mail = MagicMock()
        self.temp.template.message = MagicMock(return_value='Hi')
        self.temp.mail.send = MagicMock(side_effect=TypeError("Not a valid client"))
        self.assertRaises(TypeError, self.temp.send, None, 'Hi')

    def test_send_wrong_client_arr(self):
        self.temp.template = MagicMock()
        self.temp.mail = MagicMock()
        self.temp.template.message = MagicMock(return_value='Hi')
        self.temp.mail.send = MagicMock(side_effect=TypeError("Not a valid client"))
        self.assertRaises(TypeError, self.temp.send, [], 'Hi')

    def test_send_wrong_message_int(self):
        self.temp.template = MagicMock()
        self.temp.mail = MagicMock()
        self.temp.template.message = MagicMock(return_value='Hi')
        self.temp.mail.send = MagicMock(side_effect=TypeError("Not a valid message"))
        self.assertRaises(TypeError, self.temp.send, 'Client', 3)

    def test_send_wrong_message_None(self):
        self.temp.template = MagicMock()
        self.temp.mail = MagicMock()
        self.temp.template.message = MagicMock(return_value='Hi')
        self.temp.mail.send = MagicMock(side_effect=TypeError("Not a valid message"))
        self.assertRaises(TypeError, self.temp.send, 'Client', None)

    def test_send_wrong_message_False(self):
        self.temp.template = MagicMock()
        self.temp.mail = MagicMock()
        self.temp.template.message = MagicMock(return_value='Hi')
        self.temp.mail.send = MagicMock(side_effect=TypeError("Not a valid message"))
        self.assertRaises(TypeError, self.temp.send, 'Client', False)

    def test_send_wrong_message_True(self):
        self.temp.template = MagicMock()
        self.temp.mail = MagicMock()
        self.temp.template.message = MagicMock(return_value='Hi')
        self.temp.mail.send = MagicMock(side_effect=TypeError("Not a valid message"))
        self.assertRaises(TypeError, self.temp.send, 'Client', True)

    def test_send_wrong_message_arr(self):
        self.temp.template = MagicMock()
        self.temp.mail = MagicMock()
        self.temp.template.message = MagicMock(return_value='Hi')
        self.temp.mail.send = MagicMock(side_effect=TypeError("Not a valid message"))
        self.assertRaises(TypeError, self.temp.send, 'Client', [])

    def test_send_wrong_message_obj(self):
        self.temp.template = MagicMock()
        self.temp.mail = MagicMock()
        self.temp.template.message = MagicMock(return_value='Hi')
        self.temp.mail.send = MagicMock(side_effect=TypeError("Not a valid message"))
        self.assertRaises(TypeError, self.temp.send, 'Client', {})

    def test_receive(self):
        self.temp.mail = MagicMock()
        self.temp.mail.receive = MagicMock(return_value=True)
        self.assertTrue(self.temp.receive('Hi'))

    def test_receive_return_False(self):
        self.temp.mail = MagicMock()
        self.temp.mail.receive = MagicMock(return_value=False)
        self.assertFalse(self.temp.receive('Hi'))
