import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from RPi.GPIO import GPIO
from time import sleep
import database


def main():
    """
    Runs the main file
    :return: None
    """
    cred = credentials.Certificate("firebase_SDK.json")
    firebase_admin.initialize_app(
        cred, {
            "databaseURL": "https://weblights-513e2.firebaseio.com/",
            'databaseAuthVariableOverride': {
                'uid': 'my-service-worker'
            }})
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    pins = {
        "green": 0,
        "red": 1,
        "yellow": 2
    }
    request_numbers = 0
    while true:
        print("Making request", request_numbers + 1)
        ref = db.reference("lights").get()
        request_numbers += 1
        if ref["green"]:
            GPIO.output(pins["green"], GPIO.HIGH)
        else:
            GPIO.output(pins["green"], GPIO.LOW)
        if ref["red"]:
            GPIO.output(pins["red"], GPIO.HIGH)
        else:
            GPIO.output(pins["red"], GPIO.LOW)
        if ref["yellow"]:
            GPIO.output(pins["yellow"], GPIO.HIGH)
        else:
            GPIO.output(pins["yellow"], GPIO.LOW)
        sleep(0.5)


if __name__ == "__main__":
    main()
