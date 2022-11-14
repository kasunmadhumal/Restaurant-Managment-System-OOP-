from login import Login
from model.user import User
from utils.verify_signup import VerifySignup


class SignUp:

    @staticmethod
    def get_user_details():
        name = input(" * Please enter your name : ")
        address = input(" * Please enter your address or press enter to skip : ")
        mobile_number = input(" * Please enter your mobile number : ")
        password = input(" * Please enter your password : ")
        conform_password = input(" * Please conform your password : ")
        birthday = input(" * Please enter your date of birthday # DD/MM/YYYY (NO SPACE) : ")

        v = VerifySignup(name, address, mobile_number, password, conform_password, birthday)
        v_name_status = v.validate_name()
        v_mobile_status = v.validate_mobile_number()
        v_password_status = v.validate_password()
        v_password_matching_status = v.validate_two_passwords()
        v_birthday_date_format = v.date_format_validate()
        v_age_validate = v.user_age_validation()

        if v_name_status and v_password_status and v_mobile_status and v_password_matching_status and v_birthday_date_format and v_age_validate:
            print(" \n\n  ----> You have successfully signed up. <----")
            user_obj = User(name, address, mobile_number, password, birthday)
            return user_obj
        else:
            return 0
