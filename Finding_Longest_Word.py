# Print the longest word in the list of words given

L_list = []
def input_list_items(count1):
    Y_list = []
    val = ""
    for i in range(0, count1):
        val = str(input("Enter the word to be inserted: "))
        Y_list.append(val)

    print("Word LIST IS :  ", Y_list)
    return (Y_list)


def largest_word(count2, K_list):
    word = ""
    for i in range(0, count2 - 1):

        if len(K_list[i]) > len(K_list[i + 1]):
            word = K_list[i]
            K_list[i + 1] = word
    print ("Largest word in the list is:  ", K_list[-1])
    return (K_list)


# MAIN PROGRAM
count = int(input("Enter the count of words in the list :"))
print(" Word list ")
L_list = input_list_items(count)
print(L_list)
largest_word(count, L_list)
