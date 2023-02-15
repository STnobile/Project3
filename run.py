import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import math

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("usersdata")

# Maps category amount ranges to sheet index and category label.
MBS_USER_CATEGORY_AMOUNT = {
    (0, 350): (1, "Standard"),
    (350, 700): (2, "Advanced"),
    (700, math.inf): (3, "Elite"),
}

# Message to the user for following the application.
WELCOME_MSG = """
Welcome to Wine-Hub.net
  It is the first European platform entirely dedicated
  to buying and selling of fine wines
  and spirits for individuals and traders.

The application has 2 steps

1. Enter your data.
2. Calculate the best membership (MBS) plan for you
   which can be:
   - Standard for small businesses.
   - Advance for medium businesses.
   - Elite for wine brokers and large businesses. 
"""
CATEGORY_MSG = """
Select category:

Red
White
Rosè
Bubbles
Spitits(ex. vodka,gin,rhum)

"""


def validate_name(name):
    """ 
    This function validate the name and surname insert from the user
    and must be separated with a space.
    """
    if not len(name.split(" ")) > 2:
        print("Surname not provided. Please try again..")
        return False

    return name.title()


def input_user_name():
    """
    Here the function check if you have insert your second word or surname,
    if the user did not it will give an error and will ask the user
    to insert the data one more time.
    """
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
    """
    This function check allow the user to use one or more word to define
    the category that he chooses.
    ex. red, white, fortified wine, wodkas. and so on.
    """
    if not len(category.split(" ")) > 1:
        print(("Category not found it, please try again.."))
        return False

    return category.title()


def input_usr_category():
    """
    Allows the users to insert more than one word.
    """
    valid = False
    while not valid:
        usr_cat = input(CATEGORY_MSG)
        if not len(usr_cat.split(" ")) >= 1:
            print("Category not found it, please try again..")
            continue
        else:
            valid = True

    return usr_cat.title()


def input_user_dob():
    """
    This function check if the users insert the date of birth 
    following the format assigned.
    """
    while True:
        usr_dob = input("Insert your Date of Birth in DD/MM/YYYY format: \n ")
        try:
            return str(datetime.strptime(usr_dob, "%d/%m/%Y").date())
        except ValueError:
            print("Invalid date format. Please try again..")


def validate_amount(amount):
    """
    This function is for the user to avoid use words instead of digits.
    """
    if not amount.isdigit():
        print("Invalid amount entered..")
        return False

    return amount


def input_amount():
    """
    Here the function not allow negative number,
    in case that will be the case..
    It will give an error and will suggest to enter
    a valid data.
    """
    while True:
        try:
            user_amount = input(
                "Insert your weekly outcome on spirits & wine:\n"
            )
            user_amount = int(user_amount)
            if user_amount <= 0:
                raise ValueError("Invalid amount")
            return user_amount
        except ValueError:
            print("Please enter a valid amount.")


def get_info_data():
    """
    Get the info from the users.
    Run while loop to collect a valid data from the user,
    via terminal, which must be a string of 6 number separated by commas.
    The loop request data until it is valid.
    """

    print(WELCOME_MSG)
    usr_name = input_user_name()
    usr_dob = input_user_dob()

    usr_resid = input("Insert your residence (Ex. London): \n")

    usr_amount = input_amount()

    usr_cat = input_usr_category()

    usr_vr = input("What's your favourite style: \n")

    return [
        usr_name,
        usr_dob,
        usr_resid.title(),
        usr_amount,
        usr_cat,
        usr_vr.title(),
    ]


def update_info_worksheet(data):
    """
    Update worksheet, add new row with the list data provided
    """
    print("Analysing your data...\n")
    info_worksheet = SHEET.worksheet("info")
    info_worksheet.append_row(data)
    print("Data updated successfully.\n")


def update_mbs_worksheet(data):
    """
    Update worksheet, add new row with the list data provided
    """

    mbs_worksheet = SHEET.worksheet("mbs")
    mbs_worksheet.append_row(data)
    print("MBS updated successfully.\n")
    print("If you did not follow our form or left empy space,")
    print("you will be removed from our platform")


def calculate_mbs_usr_amount(username, usr_amount):
    """
    The MBS is our memberships plan that assign the perfect offer to the user.

    We calculate it using the AMOUNT our users inserted on the form. Once that is insert
    it will give the MBS for them.

    The MBS is calculate :
    - standard = Amount ( < 350 )
    - advance = Amount ( <= 700)
    - elite  = Amount ( > 700)
    """
    category_data = [None] * 4
    category_data[0] = username
    print("Calculating your MBS...\n")

    for category_key, category_value in MBS_USER_CATEGORY_AMOUNT.items():
        min_amount, max_amount = category_key
        if usr_amount > min_amount and usr_amount <= max_amount:
            category_sheet_index, category_label = category_value

    print(f"You are a {category_label} MBS.")
    category_data[category_sheet_index] = usr_amount
    return update_mbs_worksheet(category_data)


def main():
    data = get_info_data()
    update_info_worksheet(data)
    calculate_mbs_usr_amount(data[0], data[3])


if __name__ == "__main__":
    main()
