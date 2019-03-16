# NOTE FROM BOB: DO NOT EDIT THIS STRING
# SIGNS_GROUPS is a string representing a group for each sign:
# - Group 0 has Aries, Leo, and Saggitarius
# - Group 1 has Taurus, Virgo and Capricorn
# - Group 2 has Gemini, Libra, Aquarius
# - Group 3 has Pisces, Scorpio and Cancer
SIGN_GROUPS = '[ARI,LEO,SAG]-[TAU,VIR,CAP]-[GEM,LIB,AQU]-[PIS,SCO,CAN]'

# NOTE FROM BOB: DO NOT EDIT THIS STRING
# SIGNS is a string representing the start and end date of each sign
# Each star sign is represented using three characters (e.g. Aries = ARI)
# This is followed by a : and then the start month and start date
# and then a - and then the end month and end date
# (e.g. Aries starts on 03,21 (March 21), and ends on 04,19 (April 19))
# Each star sign's information ends with a semicolon
SIGNS = '03,21-04,19=ARI;04,20-05,20=TAU;05,21-06,21=GEM;06,22-07,22=CAN;' + \
        '07,23-08,22=LEO;08,23-09,22=VIR;09,23-10,23=LIB;10,24-11,20=SCO;' + \
        '11,21-12,21=SAG;12,22-01,20=CAP;01,21-02,21=AQU;02,22-03,20=PIS;'

def extract_month(bday):
    '''
    (str) -> int

    Given a string representing a date in the format YYYY-MM-DD, return the
    month within the string as an int.

    >> extract_month('1991-08-02')
    8

    >> extract_month('1995-12-22')
    12
    '''
    return int(bday[5:7])

def extract_date(bday):
    '''
    (str) -> int

    Given a string representing a date in the format YYYY-MM-DD, return the
    date within the string as an int.

    >> extract_date('1991-08-02')
    2

    >> extract_date('1995-12-22')
    22
    '''

    # Again: The "pass" here is a keyword that basically means 'do nothing'
    # Get rid of all these "pass" statements, as well as these comments
    # so your final code is cleaned up
    return int(bday[8:])

def count_common_occurrences(word1, word2):
    '''
    (str, str) -> int

    Given two strings, word1 and word2, return how many characters in word1 are
    letters that also occur in word2. You can assume all characters in the
    given string are lowercase. Also, spaces do not count as a common character.

    Algorithm:
    - Go through each character in word1, one by one. If this character
      occurs in word2, then add 1 to the count. Return total count after
      you're done going through the characters.

    >>> count_common_occurrences('bob y', 'bobbette z')
    3

    >>> count_common_occurrences('bobbette z', 'bob y')
    4
    '''
    co=0
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    for ch in word1:
        if ch in word2:
            co+=1
    return co


def get_sign_group(sign):
    '''
    (str) -> int

    Given a three character string representing a star sign, return
    which group (out of 0, 1, 2, or 3) this star sign belongs to.

    Use the SIGN_GROUPS string (already defined for you above) to figure
    out the group.
    i.e. As given by this string '[ARI,LEO,SAG]-[TAU,VIR,CAP]-[GEM,LIB,AQU]-[PIS,SCO,CAN]'
         the signs ARI, LEO and SAG are in group 0, the signs TAU, VIR, CAP are in group 1,
         and so on.

    >>> get_sign_group('ARI')
    0

    >>> get_sign_group('CAN')
    3
    '''
    signs=SIGN_GROUPS.replace("-","")
    for i in range (1,5):
        if sign in signs[:i*13]:
            return i-1


def find_astrological_compatibility(sign_1, sign_2):
    '''
    (str, str) -> int

    Given two 3-character strings representing star signs, return an int
    representing how compatible they are.

    According to Bob's rules, the compatibility between signs is calculated
    based on the SIGN_GROUPS they belong in, as follows:
    - If the signs are in the same group, return 100
    - If both the signs are in an odd-numbered group (i.e. 1 and 3)
      OR if both are in an even group (i.e. 0 and 2), then return 70
    - For all other cases, return 50

    >>> find_astrological_compatibility('ARI', 'LEO')
    100

    >>> find_astrological_compatibility('GEM', 'LIB')
    100

    >>> find_astrological_compatibility('SAG', 'AQU')
    70

    >>> find_astrological_compatibility('VIR', 'PIS')
    70

    >>> find_astrological_compatibility('LEO', 'TAU')
    50

    >>> find_astrological_compatibility('AQU', 'SCO')
    50
    '''
    if get_sign_group(sign_1)==get_sign_group(sign_2):
        return 100
    elif (get_sign_group(sign_1)%2)==(get_sign_group(sign_2)%2):
        return 70
    return 50

def find_astrological_sign(month, date):
    '''
    (int, int) -> str

    Given two int values representing a month and a date, return a
    3-character string that gives us what star sign a person born in that
    month and on that date belongs to. Use the SIGNS string (already
    defined for you at the top of this file) to figure this out.

    NOTE FROM BOB: A lot of string slicing to do here. It looks like the
                   information for each sign is exactly 16 characters long.
                   We can probably use that.

    >>> find_astrological_sign(8, 24)
    'VIR'

    >>> find_astrological_sign(1, 15)
    'CAP'
    '''
    signs=SIGNS.replace(";","")
    for i in range(1,13):
        signdate=signs[(i - 1) * 14 + (i - 1):i * 14 + i]
        if (int(signdate[:2])==month and  (int(signdate[3:5])<=date) or int(signdate[6:8])==month and int(signdate[9:11])>=date):
            return signdate[12:]

def get_bday_compatibility(bday1, bday2):
    '''
    (str, str) -> int

    Given two strings representing birthdates in the format YYYY-MM-DD,
    figure out what star sign each birthdate belongs to and return
    the astrological compatibility of the two signs.

    NOTE FROM BOB: This code should look similar in structure to the
                   get_name_compatibility function that I already finished.
                   That is, it should call on other functions for help,
                   and not be more than a couple of lines long in total.

    >>> get_bday_compatibility('1998-08-30', '1998-03-10')
    70

    >>> get_bday_compatibility('1998-08-10', '1998-04-01')
    100
    '''

    return find_astrological_compatibility(find_astrological_sign(extract_month(bday1), extract_date(bday1)), find_astrological_sign(extract_month(bday2), extract_date(bday2)))

#
# NOTE FROM BOB: THE FUNCTION BELOW IS DONE ALREADY. DO NOT CHANGE ANYTHING HERE.
#
def get_name_compatibility(name1, name2):
    '''
    (str, str) -> int

    Given two strings, return their name compatibility.

    According to Bob's rules, this should be calculated by checking
    how many letters in the first name occurs in the second, and
    adding this to how many letters in the second name occurs in
    the first, and then multiplying this sum by 10.

    For example:
    If the names are BOB Y and BOBBETTE Z, then
    - for BOB Y, we get the number 3, because 3 letters in this name
      occur in the other
    - for BOBBETTE Z, we get the number 4, because 4 letters in this
      name occur in the other.

    The number returned for these two names should be 3 + 4 = 7,
    multiplied by 10 = 70.

    >>> get_name_compatibility('bob y', 'bobbette z')
    70

    >>> get_name_compatibility('sadia sharmin', 'ryan gosling')
    150
    '''

    return (count_common_occurrences(name1, name2) + \
            count_common_occurrences(name2, name1)) * 10

#
# NOTE FROM BOB: THE FUNCTION BELOW IS DONE ALREADY. DO NOT CHANGE ANYTHING HERE.
#
def calculate_love_score(name1, name2, bday1, bday2):
    '''
    (str, str, str, str) -> int

    Given four strings representing two names and two birthdates in the
    format YYYY-MM-DD, return the average of the name compatibility of the
    names given and the birthdate compatibility of the birthdates given.

    NOTE FROM BOB: I'm not going to worry about checking if this number
                   is greater than 100. It's fine.
    '''

    return (get_name_compatibility(name1, name2) + \
            get_bday_compatibility(bday1, bday2)) / 2

#
# NOTE FROM BOB: THE FUNCTION BELOW IS DONE ALREADY. DO NOT CHANGE ANYTHING HERE.
#
def is_valid_date(bday):
    '''
    (str) -> bool

    Given a string, return True iff it is in the format YYYY-MM-DD, where
    each character in DD, MM, and YYYY is a number, and each are separated
    by a - character.

    >>> is_valid_date('1903-02-03')
    True

    >>> is_valid_date('1999-20-01')
    False

    >> is_valid_date('3123-310-31')
    False
    '''

    if len(bday) == 10 and bday[:4].isdigit() and bday[4] == '-' \
       and bday[5:7].isdigit() and bday[7] == '-' and bday[8:].isdigit():

        month = extract_month(bday)
        date = extract_date(bday)
        if ((month >= 1) and (month <= 12)) and \
           ((date >= 1) and (date <= 31)):
            return True

    return False

# =====================================================================
# NOTE FROM BOB:
# Do NOT change any of the lines below (feel free to comment them out
# for testing purposes though)
# p.s. remember to delete all your test stuff, and keep the code below
#      exactly the same as it is now as when you're handing it in
# =====================================================================

if __name__ == "__main__":

    name1 = input("Give me your first and last name: ")
    bday1 = input("Give me your birthdate in the format YYYY-MM-DD: ")
    while not is_valid_date(bday1):
        bday1 = input("Invalid input. Give me your birthdate in the format YYYY-MM-DD: ")

    print("=====")
    name2 = input("Give me your crush's first and last name: ")
    bday2 = input("Give me your crush's birthdate in the format YYYY-MM-DD: ")
    while not is_valid_date(bday2):
        bday2 = input("Invalid input. Give me your birthdate in the format YYYY-MM-DD: ")

    # The .lower() after the names turns all characters into lowercase so you don't
    # have to worry about comparisons taking into consideration both upper and lowercase of each letter
    print("You are " + str(calculate_love_score(name1.lower(), name2.lower(), bday1, bday2)) +"% compatible in love!")



