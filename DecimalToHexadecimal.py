
#Program to convert a given Decimal to Hexadecimal using divmod function
def decimal_to_hexa(decimal_num):
    hexa_num = remainder_portion = ""
    decimal_printvar=decimal_num
    qoutient_portion = 1
    while( qoutient_portion != 0):
        qoutient_portion = int(decimal_num//16)   # returns the qoutient portion using //
        #print(qoutient_portion)
        remainder_portion =  str(decimal_num % 16)   # returns the reminder using %
        decimal_num = qoutient_portion              #integer portion is now taken for // by 16
        hexa_num = remainder_portion+hexa_num

    print("Hexa equivalent of ",decimal_printvar,"is ",hexa_num)
    return

def conversion_using_divmod_func(decimal_number):  # using divmod function
    hexa_num = ""
    decimal_printvar = decimal_number
    qoutient_portion = 1
    while (qoutient_portion != 0):
        qoutient_portion,remainder_portion = divmod(decimal_number,16)  # this function returns qoutient and remainder
        decimal_number = qoutient_portion  #
        hexa_num = str(remainder_portion) + hexa_num
    print("Hexa equivalent of ", decimal_printvar, "is ", hexa_num,'using divmod() function.')
    return

dec_num = int(input("Enter the decimal number to be converted to hexa : "))
decimal_to_hexa(dec_num)
conversion_using_divmod_func(dec_num)
