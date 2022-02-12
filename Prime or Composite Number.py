#Check prime and composite number
# Logic for prime number-prime number is divisible by itself and 1,
# if its divisible by more than 2 numbers, then its not a prime number.
# keep the counter to 0 an its it 2 then its prime number otherwise not.

def which_is_prime(prime_number):
    pcount=0
    for i in range(1,prime_number+1):
        if (prime_number%i==0): pcount = pcount+1

    if (pcount==2):print(prime_number, " is a prime number.")  # prime number is divisible by 1 and itself(counter will be incremented only 2 times)
    else:print(prime_number,"is a composite number")  # composite number is divisible by many numbers(counter will be more than 2)
    return

prime_number = int(input("Enter the number to be checked(prime or composite: "))
which_is_prime(prime_number)

