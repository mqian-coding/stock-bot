import login

LOCAL_PATH = "/Users/mingqian/Passwords"
FILE_NAME = "rh.txt"

# Your file should be structured like:

#           username: johndoe@gmail.com
#           password: password
#           otp: mfa_otp_token


if __name__ == '__main__':
    login.login_user(LOCAL_PATH, FILE_NAME)
