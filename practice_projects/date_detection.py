#! python3
# date_detection.py Finds dates in a text

"""
What my program need to do:
1. Get the text
2. Find all dates in the text
3. Display matched strings in the screen

Step by step:
1. Create a regex that can detect all dates in the DD/MM/YYYY format. days in range from 01 to 31, months 01 to 12 and
years 1000 to 2999. If day and month is a single digit, it'll have a leading zero.
2. Create a function that can detect if it is a valid date, valid dates are: months that have only 30 days, 28 days in
february, months with 31 days and leap years.
3. Format the matched strings to one string to display
"""

import re


def date_detection(text):
    """

    :param text: Text where the dates will be searched
    :return: A list of the matching dates
    """
    date_regex = re.compile(
            r"""(
        (\d{2}|\d)          # To detect days
        [./-]               # To detect different separations
        (\d{2}|\d)          # To detect months
        [./-]               # To detect different separations
        (\d{4})             # To detect years
        )
        """,
            re.VERBOSE)
    dates = []

    # Check that days are between 1 and 31, months 1 and 12, years 1000 and 2999, and then add the to a list.
    for group in date_regex.findall(text):
        if 1 <= int(group[1]) <= 31:
            if 1 <= int(group[2]) <= 12:
                if 1000 <= int(group[3]) <= 2999:
                    dates.append(group)

    valid_dates = []
    for i in dates:

        # Appending dates in the valid_list that dont need any filtering to detect wrong dates
        if int(i[2]) not in (2, 4, 6, 9, 11):
            valid_dates.append(i)

        # Detect those dates with months have only 30 days
        elif int(i[1]) < 31 and int(i[2]) in (4, 6, 9, 11):
            valid_dates.append(i)

        # Checking if feb dates have less than 29 days
        elif int(i[2]) == 2 and int(i[1]) < 29:
            valid_dates.append(i)

        # Filtering leap years with feb months that have 29 days
        elif int(i[2]) == 2 and int(i[1]) == 29:
            if int(i[3]) % 4 == 0:
                if int(i[3]) % 100 == 0:
                    if int(i[3]) % 400 == 0:
                        valid_dates.append(i)
                else:
                    valid_dates.append(i)

    # Return valid dates and display a format string
    for dt in valid_dates:
        print(dt[0])


text = '31/13/1997, 32/05/2887, 29.02.2045, 31/06/2999, 31/12/2045, 30.08.1232, 29-02-2044'
date_detection(text)
