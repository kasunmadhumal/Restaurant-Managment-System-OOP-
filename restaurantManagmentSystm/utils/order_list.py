class OrderList:

    instance = "Null"
    order_list = []

    @staticmethod
    def get_instance():
        if OrderList.instance == "Null":
            instance = OrderList()

        return instance



