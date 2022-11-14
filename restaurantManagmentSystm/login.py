

from ordering import Ordering
from utils.users_list import UsersList


class Login:

    def __init__(self, object):
        self.user_obj = object
        self.username = ""
        self.password = ""
        self.user_login_data = []
        self.verify_user_login()

    def get_user_login_information(self):
        self.username = input(" * Please enter your username (Mobile Number) : ")
        self.password = input(" * Please enter your password : ")
        self.user_login_data = [self.username, self.password]
        return self.user_login_data




    def verify_user_login(self):
        print("\n\n ##################### Login Page #####################\n")
        while 1:
            user_data_list = self.get_user_login_information()
            signed_user_list_status = self.check_in_signed_user_list(user_data_list[0], user_data_list[1])
            if user_data_list[0] == self.user_obj.get_mobile_number() and user_data_list[1] == self.user_obj.get_password():
                print("  ---->  You have successfully login  <----\n")
                break
            elif signed_user_list_status:
                print("  ---->  You have successfully login  <----\n")
                break
            else:
                print(" * ------> Invalid Username Or Password <------")

        while 1:
            print(" * Please Enter 2.1 to start ordering.")
            print(" * Please Enter 2.2 to print statistics")
            print(" * please enter 2.3 for logout.")
            user_input = input(" * Enter: ")
            input_value = float(user_input)
            if input_value == 2.1:
                Ordering()
                break
            elif input_value == 2.2:
                from summary_of_transaction import SummaryOfTransaction
                SummaryOfTransaction()

                break
            elif input_value == 2.3:
                break
            else:
                print(" *** wrong input")


    @staticmethod
    def check_in_signed_user_list(username, password):
        user_list = UsersList().get_users_list()
        for i in range(len(user_list)):
            if user_list[i][0] == username and user_list[i][1] == password:
                return 1
                break
            return 0









