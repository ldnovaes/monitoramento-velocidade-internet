import getpass
import os
USER_NAME = getpass.getuser()


def add_to_startup_windows(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = f'C:\\Users\\{USER_NAME}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'

    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(f'python {file_path}')