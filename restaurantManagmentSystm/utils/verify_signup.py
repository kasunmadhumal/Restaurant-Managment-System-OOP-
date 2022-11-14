import datetime
from datetime import date


class VerifySignup:

    def __init__(self, name, address, mobile_number, password, conform_password, birthday):
        self.name = name
        self.address = address
        self.mobile_number = mobile_number
        self.password = password
        self.conform_password = conform_password
        self.birthday = birthday

    def validate_name(self):

        if len(self.name) > 0:
            return 1
        else:
            return 0

    def validate_mobile_number(self):
        if len(self.mobile_number) != 10:
            print(" warning: mobile number have 10 digits.")
            return 0
        else:
            return 1

    def validate_password(self):
        SpecialSym = ['$', '@', '#', '%']
        val = True

        if not any(char.isupper() for char in self.password):
            if not any(char.islower() for char in self.password):
                print(
                    " warning: The password must have the combination of alphabets, and Numeric or special character.")
                val = False

        if not any(char in SpecialSym for char in self.password):
            if not any(char.isdigit() for char in self.password):
                print(
                    " warning: The password must have the combination of alphabets, and Numeric or special character.")
                val = False

        if val:
            return val

    def validate_two_passwords(self):
        if self.password == self.conform_password:
            return 1
        else:
            print(" warning: Entered password and conformation passwords are not matching.")
            return 0

    def date_format_validate(self):
        date_string = self.birthday
        date_format = '%d/%m/%Y'
        try:
            date_obj = datetime.datetime.strptime(date_string, date_format)
            if date_obj != '':
                return 1

        except ValueError:
            print(" warning: Incorrect data format, should be DD/MM/YYYY")
            return 0

    def user_age_validation(self):

        date_birth = self.birthday
        if self.date_format_validate():
            date_m = datetime.datetime.strptime(date_birth, "%d/%m/%Y")
            birthday_year = int(date_m.year)
            current_year = int(date.today().year)
            user_age = current_year - birthday_year
            if user_age < 18:
                print(" warning: signing only for the user is at least 18 years old.")
                return 0
            else:
                return 1
        else:
            print(" warning: signing only for the user is at least 18 years old.")
            return 0
