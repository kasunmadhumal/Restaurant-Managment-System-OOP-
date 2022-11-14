
from utils.order_list import OrderList


class SummaryOfTransaction:

    def __init__(self):
        self.order_history = OrderList.get_instance().order_list
        self.get_statistics_option()


    def all_dine_orders(self):
        self.print_title()
        for i in range(len(self.order_history)):
            if self.order_history.__getitem__(i).get_type_of_order() == "dine":
                print(self.order_history.__getitem__(i).get_item_id(), "        ",
                      self.order_history.__getitem__(i).get_date(), "        ",
                      self.order_history.__getitem__(i).get_type_of_order(), "           ",
                      self.order_history.__getitem__(i).get_price())

    def all_pick_orders(self):
        self.print_title()
        for i in range(len(self.order_history)):
            if self.order_history.__getitem__(i).get_type_of_order() == "self_pickup":
                print(self.order_history.__getitem__(i).get_item_id(), "        ",
                      self.order_history.__getitem__(i).get_date(), "        ",
                      self.order_history.__getitem__(i).get_type_of_order(), "           ",
                      self.order_history.__getitem__(i).get_price())

    def all_deliveries(self):
        self.print_title()
        for i in range(len(self.order_history)):
            if self.order_history.__getitem__(i).get_type_of_order() == "home_delivery":
                print(self.order_history.__getitem__(i).get_item_id(), "        ",
                      self.order_history.__getitem__(i).get_date(), "        ",
                      self.order_history.__getitem__(i).get_type_of_order(), "           ",
                      self.order_history.__getitem__(i).get_price())

    def total_amount_spent(self):
        total_amount_spent = 0.0
        for i in range(len(self.order_history)):
            total_amount_spent += self.order_history.__getitem__(i).get_price()
        print(" *** Total amount spent on all order AUD: ", total_amount_spent)

    @staticmethod
    def print_title():
        print("\n\nOrder ID       Date         Type Of Order       Order Amount\n")

    def get_statistics_option(self):
        while 1:
            print("\n\n Please Enter the Option to Print the Statistics.")
            print(" 1. All Dine in orders.")
            print(" 2. All Pick up orders.")
            print(" 3. All Deliveries.")
            print(" 4. Total Amount Spent on All orders.")
            print(" 5. To go to previous menu.")
            user_input = int(input("Enter"))
            if user_input == 1:
                self.all_dine_orders()
            elif user_input == 2:
                self.all_pick_orders()
            elif user_input == 3:
                self.all_deliveries()
            elif user_input == 4:
                self.total_amount_spent()
            elif user_input == 5:
                from ordering import Ordering
                Ordering()
                break
