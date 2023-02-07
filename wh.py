import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("wh-users.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("usersdata")

WELCOME_MSG = """
Welcome to WH.net

Please enter your details
The data should follow the form, separated by commas.
Example: Name, Date of Birth, City, €, Categories, Grape

1. Enter your data.
2. View subscribers stats
"""


def validate_name(name):
    if not len(name.split(" ")) > 2:
        print("Surname not provided. Please try again..")
        return False

    return name.title()


def input_user_name():
    valid = False
    while not valid:
        usr_name = input("Insert your Name and Surname: \n")
        if not len(usr_name.split(" ")) >= 2:
            print("Surname not provided. Please try again..")
            continue
        else:
            valid = True

    return usr_name.title()

    # user_name = validate_name(user_name)
    # if not user_name:
    #     continue




def validate_amount(amount):
    if not amount.isdigit():
        print("Invalid amount entered..")
        return False

    return amount


def validate_dob(dob):
    try:
        return datetime.strptime(dob, "%m/%d/%Y")
    except ValueError:
        print("Invalid date format. Please try again..")
        return False


def get_info_data():
    """
    Get the info from the users.
    Rub while loop to collect a valid data from the user,
    via terminal, which must be a string of 6 number separated by commas.
    The loop request data until it is valid.
    """
    # while True:
    print(WELCOME_MSG)
    usr_name = input_user_name()

    usr_dob = input("Insert your Date of Birth in MM/DD/YYYY format: \n ")

    usr_residency = input("Insert your Residency (Ex. London): \n")

    usr_amount = input("Insert your Amount: \n")

    usr_category = input_usr_category()

    usr_vr = input("Insert your Grape varieties: \n")

    # info_data = data_str.title()

    # if validate_data(info_data):
    #     print("Data is valid!")
    #     break

    # return info_data

    return [usr_name, usr_dob, usr_residency, usr_amount, usr_category, usr_vr]


# def validate_data(values):
#    """
#    Here, we converts the strings to integers.
#    Set the value error if it wont respect the int,
#    or if the users insert more info.
#    """
#    try:
#        # Name, Date of Birth, City, Amount, Category, Grape varieties.
#        if len(values) != 25:
#            raise ValueError(f"Required 6 value, {len(values)}")
#    except ValueError as e:
#        print(f"Invalid data : {e}, try again.\n")
#        return False

#    return True


def update_info_worksheet(data):
    """
    Update worksheet, add new row with the list data provided
    """
    print("Updating worksheet...\n")
    info_worksheet = SHEET.worksheet("info")
    info_worksheet.append_row(data)
    print("Worksheet updated successfully.\n")


if __name__ == "__main__":
    data = get_info_data()
    update_info_worksheet(data)


# Welcome message
# 1. Input my data
# a. View my membership
# b.
