import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import math

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("wh-users.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("usersdata")

# Maps category amount ranges to sheet index and category label.
MBS_USER_CATEGORY_AMOUNT = {
    (0, 350): (1, "Standard"),
    (350, 700): (2, "Advanced"),
    (700, math.inf): (3, "Elite"),
}

WELCOME_MSG = """
Welcome to WH.net

Please enter your details
The data should follow the form. Pay attention to the EX.
Example: Name, Date of Birth, City, amount, Categories, Grape.

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


def validate_category(category):
    if not len(category.split(" ")) >= 1:
        print(("Category not found it, please try again.."))
        return False

    return category.title()


def input_usr_category():
    valid = False
    while not valid:
        usr_category = input(
            "Insert your favorite wine Category.(Ex.Red,White)\n"
        )
        if not len(usr_category.split(" ")) >= 1:
            print("Category not found it, please try again..")
            continue
        else:
            valid = True

    return usr_category.title()


def validate_amount(amount):
    if not amount.isdigit():
        print("Invalid amount entered..")
        return False

    return amount


def input_user_dob():
    while True:
        usr_dob = input("Insert your Date of Birth in MM/DD/YYYY format: \n ")
        try:
            return str(datetime.strptime(usr_dob, "%m/%d/%Y"))
        except ValueError:
            print("Invalid date format. Please try again..")


# def input_user_category():
#     CATEGORY_MSG = """
#     Select category:
#     1. Red
#     2. White
#     """
#     while True:
#         usr_category = input(CATEGORY_MSG)
#         try:
#             return datetime.strptime(usr_dob, "%m/%d/%Y")
#         except ValueError:
#             print("Invalid date format. Please try again..")


def input_amount():
    while True:
        try:
            user_amount = input("Insert your Amount: \n")
            user_amount = int(user_amount)
            if user_amount <= 0:
                raise ValueError("Invalid amount")
            return user_amount
        except ValueError:
            print("Please enter a valid amount.")


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
    usr_dob = input_user_dob()

    usr_residency = input("Insert your Residency (Ex. London): \n")

    usr_amount = input_amount()

    usr_category = input_usr_category()

    usr_vr = input("Insert your Grape varieties: \n")

    return [usr_name, usr_dob, usr_residency, usr_amount, usr_category, usr_vr]


def update_info_worksheet(data):
    """
    Update worksheet, add new row with the list data provided
    """
    print("Updating worksheet...\n")
    info_worksheet = SHEET.worksheet("info")
    info_worksheet.append_row(data)
    print("Worksheet updated successfully.\n")


def update_mbs_worksheet(data):
    """
    Update worksheet, add new row with the list data provided
    """
    print("Updating worksheet...\n")
    mbs_worksheet = SHEET.worksheet("mbs")
    mbs_worksheet.append_row(data)
    print("Worksheet updated successfully.\n")


def calculate_mbs_usr_amount(username, usr_amount):
    category_data = [None] * 4
    category_data[0] = username

    for category_key, category_value in MBS_USER_CATEGORY_AMOUNT.items():
        min_amount, max_amount = category_key
        if usr_amount > min_amount and usr_amount <= max_amount:
            category_sheet_index, category_label = category_value

    print(f"You are a {category_label} MBS.")
    category_data[category_sheet_index] = usr_amount
    return update_mbs_worksheet(category_data)

    # if usr_amount < 350:
    #     print("You are a Standard MBS")
    # elif usr_amount <= 700:
    #     print("You are an Advanced MBS")
    # else:
    #     print("You are an Elite MBS")


def calculate_mbs_data(data):
    """
    The MBS is our memberships plan that assign the perfect offer to the user.

    We calculate it using the AMOUNT our user insert. Once that is insert
    it will give the MBS for them.

    The MBS is calculate :
    - standard = Amount ( < 350 )
    - advance = Amount ( <= 700)
    - elite  = Amount ( > 700)
    """
    print("You are being eligible for the MBS..\n")
    # row_count = SHEET.worksheet("mbs").row_count
    # print(row_count)
    # print(data)
    # the_value = SHEET.worksheet("mbs").cell(row_count, 3).value
    the_value = data[3]
    print(the_value)


def main():
    data = get_info_data()
    update_info_worksheet(data)
    # calculate_mbs_data(data)
    calculate_mbs_usr_amount(data[0], data[3])
    # update_mbs_worksheet([data[0], data[3]])


if __name__ == "__main__":
    main()
