import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import platform
import os


def update_pulse(consecutive_number_of_runs, service_name):
    """Updates the pulse for this application
    Arguments:
        consecutive_number_of_runs {int} -- how many times the application has ran in a row
        service_name {str} -- name of the service
    Returns:
        dict -- what the pulse was set as in the database
    """
    current_time = str(datetime.now())
    ref = db.reference("pulses/" + service_name)
    if "linux" in str(platform.platform()).lower():
        ip_command = str(os.popen("hostname -I").read())
        ip = ip_command.split(" ")[0]
    else:
        ip = ""
    ref_set = {
        "Pulse-Time": current_time,
        "Pulse-Amount-(Consecutive)": consecutive_number_of_runs,
        "Pulse-Node": str(platform.uname().node),
        "Pulse-OS": str(platform.platform()),
        "Pulse-Python-Version": str(platform.python_version()),
        "Pulse-IP": ip
    }
    ref.set(ref_set)
    return ref_set


# Testing:
# cred = credentials.Certificate("firebase_SDK.json")
# firebase_admin.initialize_app(
#     cred, {
#         "databaseURL": "https://weblights-513e2.firebaseio.com/",
#         'databaseAuthVariableOverride': {
#             'uid': 'my-service-worker'
#         }})
# update_pulse(0, "Backend")
