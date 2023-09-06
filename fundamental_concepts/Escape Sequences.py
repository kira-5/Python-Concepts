weather = "It's sunny"

# ? Escape sequence : \
weather = "It's \"kind of\" sunny"
# * Whaterver comes after backslash('\'), asuume that is a string.
print(weather)
# * 1. used for put single or double quote inside string.

weather = "It\\s \"kind of\" sunny"
print(weather)

# ? Tan spacing : \t
weather = "\t It\'s \"kind of\" sunny"
print(weather)

# ? New Line: \n
weather = "\t It\'s \"kind of\" sunny \n hope you had a good day"
print(weather)
