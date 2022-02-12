K_list=[]
num = 0

def nine_values_fibonacci_series(K_list):
    #Generate fibonacci series in this for loop
    a=0
    b=1
    i=0
    num=0
    for i in range(0,9):
        num=a+b
        K_list.insert(i,num)
        a=b
        b=num
    print ("List is   ", K_list)
    T_tuple=tuple(K_list)
    print("Tuple value is ",T_tuple)
    return (K_list)


# MAIN PROGRAM

nine_values_fibonacci_series(K_list)