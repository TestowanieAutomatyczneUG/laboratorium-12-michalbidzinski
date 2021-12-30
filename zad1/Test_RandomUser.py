import unittest
from RandomUser import RandomUser
from unittest.mock import *
from assertpy import assert_that


class TestRandomUser(unittest.TestCase):
    def setUp(self):
        self.temp = RandomUser()

    def test_get_email(self):
        assert_that(self.temp.get_email()).ends_with('@example.com')

    def test_get_email_2(self):
        assert_that(self.temp.get_email()).is_instance_of(str)

    def test_get_random_user(self):
        assert_that(self.temp.get_random_user()).is_instance_of(dict)

    def test_get_random_user_male_is_dict(self):
        assert_that(self.temp.get_random_user_gender('male')).is_instance_of(dict)

    def test_get_random_user_male(self):
        self.assertEqual(self.temp.get_random_user_gender('male')["gender"], "male")

    def test_get_random_user_female_is_dict(self):
        assert_that(self.temp.get_random_user_gender('female')).is_instance_of(dict)

    def test_get_random_user_female(self):
        self.assertEqual(self.temp.get_random_user_gender('female')["gender"], "female")

    def test_get_random_user_gender_int(self):
        self.assertRaises(Exception, self.temp.get_random_user_gender, 2)

    def test_get_random_user_gender_not_a_existing_gender(self):
        self.assertRaises(Exception, self.temp.get_random_user_gender, "hippo")

    def test_get_random_user_gender_arr(self):
        self.assertRaises(Exception, self.temp.get_random_user_gender, [])

    def test_get_random_user_gender_obj(self):
        self.assertRaises(Exception, self.temp.get_random_user_gender, {})

    def test_get_random_user_gender_None(self):
        self.assertRaises(Exception, self.temp.get_random_user_gender, None)

    def test_get_random_user_gender_False(self):
        self.assertRaises(Exception, self.temp.get_random_user_gender, False)


class TestRandomUserMock(unittest.TestCase):
    def setUp(self):
        self.temp = RandomUser()

    def test_get_email(self):
        self.temp.get_email = MagicMock()
        self.temp.get_email.return_value = {
            "email": "brad.gibson@example.com"
        }
        self.assertEqual({
            "email": "brad.gibson@example.com"
        }, self.temp.get_email())

    def test_get_random_user(self):
        random_user = {"results": [
            {"gender": "male", "name": {"title": "Mr", "first": "Umit", "last": "Christenhusz"},
             "location": {"street": {"number": 3958, "name": "Burgemeester Mazairaclaan"}, "city": "Zwaagdijk-West",
                          "state": "Drenthe", "country": "Netherlands", "postcode": 79704,
                          "coordinates": {"latitude": "45.4432", "longitude": "-118.0848"},
                          "timezone": {"offset": "-5:00", "description": "Eastern Time (US & Canada), Bogota, Lima"}},
             "email": "umit.christenhusz@example.com",
             "login": {"uuid": "e1463f0c-91ae-406e-82ee-56713d74e069", "username": "whitetiger435", "password": "bunny",
                       "salt": "KfQ3aA7q", "md5": "a9a584ea0b22451867d0997205001ab6",
                       "sha1": "4c7f8d00e1da34687b4746090d4bc59ec554f7f2",
                       "sha256": "fe6bceeb2eecc15d183ea8264b78967c4840217c34c89a151d8d31f539916194"},
             "dob": {"date": "1965-07-16T03:50:32.102Z", "age": 56},
             "registered": {"date": "2010-09-10T23:03:09.384Z", "age": 11}, "phone": "(284)-280-4648",
             "cell": "(019)-755-8271", "id": {"name": "BSN", "value": "36928275"},
             "picture": {"large": "https://randomuser.me/api/portraits/men/11.jpg",
                         "medium": "https://randomuser.me/api/portraits/med/men/11.jpg",
                         "thumbnail": "https://randomuser.me/api/portraits/thumb/men/11.jpg"}, "nat": "NL"}],
            "info": {"seed": "2c2ece6e981f5626", "results": 1, "page": 1, "version": "1.3"}}
        self.temp.get_random_user = MagicMock(return_value=random_user)
        self.assertEqual(self.temp.get_random_user(), random_user)

    def test_get_random_user_with_gender(self):
        random_user = {"results": [
            {"gender": "male", "name": {"title": "Mr", "first": "Umit", "last": "Christenhusz"},
             "location": {"street": {"number": 3958, "name": "Burgemeester Mazairaclaan"}, "city": "Zwaagdijk-West",
                          "state": "Drenthe", "country": "Netherlands", "postcode": 79704,
                          "coordinates": {"latitude": "45.4432", "longitude": "-118.0848"},
                          "timezone": {"offset": "-5:00", "description": "Eastern Time (US & Canada), Bogota, Lima"}},
             "email": "umit.christenhusz@example.com",
             "login": {"uuid": "e1463f0c-91ae-406e-82ee-56713d74e069", "username": "whitetiger435", "password": "bunny",
                       "salt": "KfQ3aA7q", "md5": "a9a584ea0b22451867d0997205001ab6",
                       "sha1": "4c7f8d00e1da34687b4746090d4bc59ec554f7f2",
                       "sha256": "fe6bceeb2eecc15d183ea8264b78967c4840217c34c89a151d8d31f539916194"},
             "dob": {"date": "1965-07-16T03:50:32.102Z", "age": 56},
             "registered": {"date": "2010-09-10T23:03:09.384Z", "age": 11}, "phone": "(284)-280-4648",
             "cell": "(019)-755-8271", "id": {"name": "BSN", "value": "36928275"},
             "picture": {"large": "https://randomuser.me/api/portraits/men/11.jpg",
                         "medium": "https://randomuser.me/api/portraits/med/men/11.jpg",
                         "thumbnail": "https://randomuser.me/api/portraits/thumb/men/11.jpg"}, "nat": "NL"}],
            "info": {"seed": "2c2ece6e981f5626", "results": 1, "page": 1,
                     "version": "1.3"}}
        self.temp.get_random_user_gender = MagicMock(return_value=random_user)
        self.assertEqual(self.temp.get_random_user_gender(), random_user)

    def tearDown(self):
        self.temp = None
