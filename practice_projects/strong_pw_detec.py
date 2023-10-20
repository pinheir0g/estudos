#! python3
# strong_passwd_detection.py  Check if the password that was passed is strong

"""
What this program needs to do:
1 - get the user password.
2 - verify if the password received is strong.
3 - Show a message telling if the password is strong or not.

Step by step:
1 - Write a regular expression that checks if the password is within the conditions:
    a. Have at least eight characters long.
    b. contains both uppercase and lowercase characters.
    c. has at least one digit.
2 - If the password was strong, show a massage telling that the user was registered successfully
if it is not strong, ask to enter a new password within the necessary parameters.
"""
import re

def strong_passwd():
    """
    Verify if the password received is strong
    :return: A message telling if the password is strong or not
    """
    passwd_regex = re.compile(r'(\w*[A-Z.!@#$%]\w*)')
    passwd = []

    # Get the user username
    user = input('Username: ')

    # Create a loop to get only a valid password
    while True:
        pw = input('Password: ')

        # Check if the password has at least 8 characters long
        for pwd in passwd_regex.findall(pw):
            if len(pwd) >= 8:
                passwd.append(pwd)

        if len(passwd) > 0:
            print('User Registered Successfully!')
            break
        else:
            print('\033[31mInvalid Password!\033[m')
            print('''The password must contain the following characters:
    - 8 or more characters long;
    - At least 1 digit;
    - 1 or more characters uppercase and lowercase.''')


strong_passwd()
