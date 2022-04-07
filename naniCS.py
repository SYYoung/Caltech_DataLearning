def CheckCorrectDay():
    '''
    :param whichDay: the user input.
    check if it is Monday, Tuesday, Wednesday, Thursday or Friday.
    If it is one of them, return True. Otherwise, return False
    :return: True if the day is weekend. False if it is not.
    '''
    weekday_list = ["monday", "tuesday", "wednesday", "thursday", "friday"]

    correct_day = False
    while not correct_day:
        day = input("Enter the day. it must be weekday: Monday through Friday.\n")
        the_day = day.lower()
        if (the_day in weekday_list):
            correct_day = True
    return the_day

def CheckStart():
    cmd1 = input("Would you like to calculate? Press Yes or yes if you would like to contine.\n")
    if  (cmd1 == 'Yes' or cmd1 == 'yes'):
        return True
    else:
        return False

def CheckKeyword(the_day):
    Monday = ["Fruit", "Apple", "Orange"]
    Tuesday = ["Sport", "Basketball", "Running"]
    Wednesday = ["Car", "BMW", "Toyota"]
    Thursday = ["Phone", "iPhone", "Samsung"]
    Friday = ["Subject", "Computer", "Math"]

    correct = False
    while not correct:
        keyword = input("Please enter the keyword.\n")
        if the_day == "monday":
            correct = keyword in Monday
        elif the_day == "tuesday":
            correct = keyword in Tuesday
        elif the_day == "wednesday":
            correct = keyword in Wednesday
        elif the_day == "thursday":
            correct = keyword in Thursday
        elif the_day == "friday":
            correct = keyword in Friday

HOURLY_PAY = 8
def CalculatePay():
    hours = int(input("How many hours will you work.\n"))
    pay = HOURLY_PAY * hours
    print("Your paid is: ", pay)

## 1. get the command to see if the user want to run the program
start = True
while start:
    start = CheckStart()
    ## 2. Now the user must type in the day correct. It must be weekday
    if start:
        which_day = CheckCorrectDay()
        if which_day:
            ## 3. Check the keyword
            CheckKeyword(which_day)
            CalculatePay()