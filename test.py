import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
from gspread.utils import rowcol_to_a1

# use creds to create a client to interact with the Google Drive API
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.

sheet = client.open("infrastructure test").sheet1

for row in range(4):
    for column in range(2):
        print(sheet.cell(row + 1, column + 1).value)

sheet.update_cell(1, 1, "Updated at %s" % time.asctime())

col = 1
for row in range(3, 6):
    address = sheet.cell(row + 1, col).value
    email = address.split("@")
    user = email[0]
    domain = email[1]
    extraneous = email[2:]
    print(email)
    if user and domain == "helpfulengineering.org" and not extraneous:
        print("email is good")
        sheet.format(
            rowcol_to_a1(row + 1, col),
            {"backgroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0}},
        )
    else:
        sheet.format(
            rowcol_to_a1(row + 1, col),
            {"backgroundColor": {"red": 1.0, "green": 0.0, "blue": 0.0}},
        )
