from model.order_item import OrderItem


from utils.order_list import OrderList


class Menu:

    order_list = OrderList.get_instance().order_list

    def __init__(self, ordering_mode):
        self.ordering_mode = ordering_mode
        self.show_menu()

    def add_to_list(self, item_id, name, price,type_of_order):
        self.order_list.append(OrderItem(item_id, name, price,type_of_order))

    def get_ordered_list(self):
        return self.order_list

    def handling_orders(self, item_id, type_of_order):

        if item_id == 1:
            self.add_to_list("1", "Noodles", 2, type_of_order)
        elif item_id == 2:
            self.add_to_list("2", "Sandwich", 4, type_of_order)
        elif item_id == 3:
            self.add_to_list("3", "Dumpling", 6, type_of_order)
        elif item_id == 4:
            self.add_to_list("4", "Muffins", 8, type_of_order)
        elif item_id == 5:
            self.add_to_list("5", "Pasta", 10, type_of_order)
        elif item_id == 6:
            self.add_to_list("6", "Pizza", 20, type_of_order)
        elif item_id == 8:
            self.add_to_list("8", "Coffee", 20, type_of_order)
        elif item_id == 9:
            self.add_to_list("9", "Cold_drink", 20, type_of_order)
        elif item_id == 10:
            self.add_to_list("10", "Shake", 20, type_of_order)

    def show_menu(self):
        while 1:
            print("        ID     NAME                PRICE")
            print("Enter   1      Noodles             AUD 2")
            print("Enter   2      Sandwich            AUD 4")
            print("Enter   3      Dumpling            AUD 6")
            print("Enter   4      Muffins             AUD 8")
            print("Enter   5      Pasta               AUD 10")
            print("Enter   6      Pizza               AUD 20")

            if self.ordering_mode == "dine":
                print("Enter   8      Coffee               AUD 20")
                print("Enter   9      Cold_drink           AUD 20")
                print("Enter   10      Shake                AUD 20")

            else:
                print("Enter   7 for  Drinks Menu                ")

            print("Enter   11 for  CHECKOUT                   ")
            user_input = int(input(" * Enter: "))
            if user_input == 7:
                print("\n\n################ Drinks #####################\n")
                print("Enter   8      Coffee               AUD 20")
                print("Enter   9      Cold_drink           AUD 20")
                print("Enter   10      Shake                AUD 20")
            elif user_input == 11:
                order_amount = 0.0

                list_of_order = self.get_ordered_list()
                for i in range(len(list_of_order)):
                    order_amount += float(list_of_order.__getitem__(i).get_price())

                service_charges = order_amount * 0.1
                total_amount = service_charges + order_amount

                if self.ordering_mode == "dine":
                    print("\n Your total payable amount is : ", total_amount, " including ", service_charges, " for service charges")
                elif self.ordering_mode == "self_pickup":
                    print("\n Your total payable amount is : ", order_amount)
                elif self.ordering_mode == "home_delivery":
                    print("\n Your total payable amount is :", order_amount, " and there will be an additional charges for delivery.")
                    print("\n ########## A fix charges for delivery base on the distance.############\n")
                    print(" * More than 0 to 2kms      AUD 5")
                    print(" * More than 2 to 5kms      AUD 10")
                    print(" * More than 5kms           No Delivery provided")



                while 1:
                    print("\n\n ** Please Enter 'Y' to conform the order , or 'N' to cancel.")
                    user_conformation = input(" * Enter : ")
                    if user_conformation == 'Y' or user_conformation == "y":
                        print("Thank you for the confirmation, Your Order has been confirmed.\n\n")
                        from ordering import Ordering
                        Ordering()
                        break
                    elif user_conformation == 'N' or user_conformation == "n":
                        print("Your Order has been canceled.")
                        from ordering import Ordering
                        Ordering()
                        break
                    else:
                        print(" *** Wrong value Entered ***")


                break

            self.handling_orders(user_input, self.ordering_mode)
