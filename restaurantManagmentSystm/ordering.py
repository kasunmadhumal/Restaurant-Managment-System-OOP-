from online_order_options import OnlineOrederingOptions



class Ordering:

    def __init__(self):
        self.show_ordering_options()
        self.ordering_mode = ""


    def show_ordering_options(self):
        print(" \n################ Ordering Modes #################\n")
        print("Please enter 1 for Dine in.")
        print("Please enter 2 for order online .")
        print("Please enter 3 to go to Login Page.")
        user_input = int(input(" * Enter: "))

        if user_input == 1:
            self.ordering_mode = "dine"
            from utils.menu import Menu
            Menu(self.ordering_mode)
        elif user_input == 2:
            OnlineOrederingOptions()
        elif user_input == 3:
            from login import Login
            from model.user import User
            Login(User("", "", "", "", ""))
