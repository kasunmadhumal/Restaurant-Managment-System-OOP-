class User:

    def __init__(self, name, address, mobile_number, password, birthday):
        self.name = name
        self.address = address
        self.mobile_number = mobile_number
        self.password = password
        self.birthday = birthday

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_mobile_number(self):
        return self.mobile_number

    def get_password(self):
        return self.password

    def get_birthday(self):
        return self.birthday

    def set_name(self,s_name):
        self.name = s_name

    def set_address(self,s_address):
        self.address = s_address

    def set_mobile_number(self,s_mobile_number):
        self.mobile_number = s_mobile_number

    def set_password(self,s_password):
        self.password = s_password

    def set_birthday(self,s_birthday):
        self.birthday = s_birthday
