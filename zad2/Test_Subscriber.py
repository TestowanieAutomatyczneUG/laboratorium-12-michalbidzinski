import unittest
from unittest.mock import *
from Subscriber import Subscriber


class TestSubscriber(unittest.TestCase):
    def setUp(self):
        self.temp = Subscriber()

    def test_add_client(self):
        self.temp.add_client = MagicMock(return_value=['Klientela'])
        self.assertEqual(["Klientela"], self.temp.add_client())

    def test_add_client_int(self):
        self.temp.add_client = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.add_client, 3)

    def test_add_client_obj(self):
        self.temp.add_client = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.add_client, {})

    def test_add_client_arr(self):
        self.temp.add_client = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.add_client, [])

    def test_add_client_arr1(self):
        self.temp.add_client = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.add_client, ["git"])

    def test_add_client_None(self):
        self.temp.add_client = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.add_client, None)

    def test_delete_client(self):
        self.temp.delete_client = MagicMock(return_value=[])
        self.assertEqual([], self.temp.delete_client('Klientela'))

    def test_delete_client_not_existing(self):
        self.temp.delete_client = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.delete_client, "marek")

    def test_delete_client_False(self):
        self.temp.delete_client = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.delete_client, False)

    def test_delete_client_True(self):
        self.temp.delete_client = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.delete_client, True)

    def test_delete_client_None(self):
        self.temp.delete_client = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.delete_client, None)

    def test_delete_client_int(self):
        self.temp.delete_client = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.delete_client, 3)

    def test_send_message(self):
        self.temp.send_message = MagicMock(return_value=True)
        self.assertTrue(self.temp.send_message("Klientela", "Hi"))

    def test_send_message_not_such_client(self):
        self.temp.send_message = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.temp.send_message, 333, "hi")

    def test_send_message_wrong_client_and_message(self):
        self.temp.send_message = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.send_message, 13, None)

    def test_send_message_wrong_client_and_message_2(self):
        self.temp.send_message = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.send_message, [], [])

    def test_send_message_wrong_client_and_message_3(self):
        self.temp.send_message = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.send_message, {}, {})

    def test_send_message_wrong_message(self):
        self.temp.send_message = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.send_message, "Klientela", False)

    def test_send_message_wrong_message_2(self):
        self.temp.send_message = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.send_message, "Klientela", [])

    def test_send_message_wrong_message_3(self):
        self.temp.send_message = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.temp.send_message, "Klientela", {})
