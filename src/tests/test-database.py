import unittest
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import sys

sys.path.append("..")
import database


class TestDatabase(unittest.TestCase):
    """
    Tests for the database.py file
    """

    def test_update_pulse(self):
        """
        Test for the update_pulse function
        """
        service_name = ""
        cred = credentials.Certificate("./../firebase_SDK.json")
        firebase_admin.initialize_app(
            cred, {
                "databaseURL": "https://weblights-513e2.firebaseio.com/",
                'databaseAuthVariableOverride': {
                    'uid': 'my-service-worker'
                }})
        instance = database.update_pulse(1, service_name)
        ref = db.reference("pulses/" + service_name)
        ref_data = ref.get()
        self.assertEqual(instance, ref_data)


if __name__ == "__main__":
    unittest.main()
