#Rotating the elements of a list-first element moves to the second position and the last element comes to the first position
def input_list_items(count1):
    Y_list = []
    for i in range(0, count1):
        value = int(input("Enter the value: "))
        Y_list.insert(i, value)
    print("ORIGINAL LIST IS :  ",Y_list)
    return(Y_list)

def rotate(count2,K_list):
    Z_list=[]

    for i in range(count2-1):
        val=K_list[i]
        K_list[i]= K_list[i+1]
        K_list[i + 1] = val
    print ("ROTATED LIST IS:  ",K_list)
    return(K_list)

#MAIN PROGRAM
count=int(input("Enter the length of the list :"))
print(" NEW list ")
L_list=input_list_items(count)
print(L_list)
rotate(count,L_list)

