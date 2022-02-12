month_dictionary = {}


def dictionary_creation(month_dictionary):
    month_name_as_key = ""
    days_as_value = 0
    count = int(input("Enter the number of elements in the dictionary:  "))
    for i in range(count):
        month_name_as_key = str(input("Enter the name of the month:  "))
        days_as_value = int(input("Enter the number of days in this month:  "))
        month_dictionary.update({month_name_as_key: days_as_value})
    return (month_dictionary)


def find_days(month_dictionary):
    user_input_month = input("Enter the month to be searched for: ")
    if user_input_month in month_dictionary:
        month_name = month_dictionary.get(user_input_month)
    return (month_name)


def allkey_in_alphabeticalorder(month_dictionary):
    list_month_keys = []
    list_month_keys = month_dictionary.keys()
    print(list_month_keys)
    list_month_keys = list_month_keys.sort()
    print(list_month_keys)
    return (list_month_keys)


# MAIN PROGRAM

print("Main function output:", dictionary_creation(month_dictionary))
# print("The days in this month is :",find_days(month_dictionary))
allkey_in_alphabeticalorder(month_dictionary)
