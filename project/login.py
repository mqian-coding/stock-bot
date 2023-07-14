import os
import pyotp
import robin_stocks.robinhood as rh


def get_login_info(local_path: str, file_name: str) -> (str, str):
    username, password, otp = "", "", ""
    file_path = os.path.join(local_path, file_name)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            u, p = file.read().split("\n")
            username, password = u.split("username: ")[1], p.split("password: ")[1]
    return username, password


def login_user(sign_in_path: str, sign_in_file_name: str):
    username, password, otp = get_login_info(sign_in_path, sign_in_file_name)
    totp = pyotp.TOTP(otp).now()
    login = rh.login(username, password, mfa_code=totp)
