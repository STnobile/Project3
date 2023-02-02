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


def get_info_users_data():
    """ 
    Get the info from the users
    """
    print("Please enter your details")
    print("The data should follow the form, separated by commas.")
    print("Example: Name,Data of Birth,City,Amount,Categories,Grape varieties.\n")

    data_str = input("Insert your data here: \n")
    print(f'The data is {data_str}')


get_info_users_data()