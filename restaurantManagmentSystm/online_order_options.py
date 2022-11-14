from utils.menu import Menu



class OnlineOrederingOptions:

    def __init__(self):
        self.ways_of_online_ordering()
        self.ordering_mode = ""



    def ways_of_online_ordering(self):
        print("\n ############ Online ordering options #############\n")
        print(" * Enter 1 for self pickup.")
        print(" * Enter 2 for Home delivery")
        print(" * Enter 3 to go to previous menu.")

        user_input = int(input(" * Enter:"))

        while 1:
            if user_input == 1:
                self.ordering_mode = "self_pickup"
                Menu(self.ordering_mode)
                break
            elif user_input == 2:
                self.ordering_mode = "home_delivery"
                Menu(self.ordering_mode)
                break
            elif user_input == 3:
                from ordering import Ordering
                Ordering()
                break
            else:
                print(" * wrong input.")

