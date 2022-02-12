#Decimal to Binary convertion
def decimal_to_binary(decimal_num):
    binary_num = remainder_portion = ""
    decimal_printvar=decimal_num
    qoutient_portion = 1
    while( qoutient_portion != 0):
        qoutient_portion = int(decimal_num//2) # returns the qoutient portion using //
        #print(qoutient_portion)
        remainder_portion =  str(decimal_num % 2)   # returns the reminder using %
        decimal_num = qoutient_portion              #integer portion is now taken for // by 2
        binary_num = remainder_portion+binary_num
    print("Binary equivalent of ",decimal_printvar,"is ",binary_num)
    return

def conversion_using_divmod_func(decimal_number):  # using divmod function
    binary_num = ""
    decimal_printvar = decimal_number
    qoutient_portion = 1
    while (qoutient_portion != 0):
        qoutient_portion,remainder_portion = divmod(decimal_number,2)  # this function returns qoutient and remainder
        decimal_number = qoutient_portion  #
        binary_num = str(remainder_portion) + binary_num
    print("Binary equivalent of ", decimal_printvar, "is ", binary_num,'using divmod() function.')
    return

dec_num = int(input("Enter the decimal number to be converted: "))
decimal_to_binary(dec_num)
conversion_using_divmod_func(dec_num)

