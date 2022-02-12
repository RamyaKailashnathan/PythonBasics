

#Program to check if the year stored in a list is a leap year or not
def is_year_leap(year):
    if (year % 4 == 0):
        return True

def days_in_month(year, month):
    if ((is_year_leap(year) == True) and (month == 2)):
        return (29)


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)

    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

