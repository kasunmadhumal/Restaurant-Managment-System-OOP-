from login import Login
from model.user import User
from signup import SignUp


class HomePage:
    def __init__(self):
        self.get_user_option()

    @staticmethod
    def get_user_option():
        print(" * Please Enter 1 for Signup. \n * Please Enter 2 for Login. \n * Please Enter 3 for Exit.")
        user_input = int(input(" Enter : "))

        if user_input == 1:

            while 1:
                sign_up_page = SignUp().get_user_details()
                if sign_up_page != 0:
                    Login(sign_up_page)
                    break

        elif user_input == 2:
            Login(User("", "", "", "", ""))
        elif user_input == 3:
            exit()
