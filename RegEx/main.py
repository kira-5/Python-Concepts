import re


date_string = '10/04/2022'
date_regex = "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"
if re.match(date_regex, date_string):
    print(True)
else:
    print(False)
