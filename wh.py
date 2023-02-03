import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('wh-users.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('usersdata')


def get_info_data():
    """ 
    Get the info from the users.
    Rub while loop to collect a valid data from the user,
    via terminal, which must be a string of 6 number separated by commas.
    The loop request data until it is valid.
    """
    while True: 
         print("Please enter your details")
         print("The data should follow the form, separated by commas.")
         print("Example: Name,Data of Birth,City,Amount,Categories,Grapevarieties.\n")

    
         data_str = input("Insert your data here: \n")     
         info_data = data_str.split(",")
    
         if validate_data(data):
            print("Data is valid!")
            break
    
    return info_data


def validate_data(values):
    """
    Here, we converts the strings to integers.
    Set the value error if it wont respect the int,
    or if the users insert more info.
    """
    try:
        [len(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Required 6 value, {len(values)}"
            )
    except ValueError as e:
         print(f"Invalid data : {e}, try again.\n")
         return False  

    return True


def update_info_worksheet(data):
    """
    Update worksheet, add new row with the list data provided
    """
    print("Updating worksheet...\n")
    info_worksheet = SHEET.worksheet("info")
    info_worksheet.append_row(data)
    print("Worksheet updated successfully.\n")


data = get_info_data()
info_data = [len(value) for value in data]
update_info_worksheet(info_data)