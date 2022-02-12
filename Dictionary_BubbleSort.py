dict0=dict1 = dict2 = dict3 = {}
list1=[]
count=0
def dict_creation(count, dict0):
    key1=value1=0
    for i in range(count):
        key1= int(input("Enter the key  :"))
        value1 = int(input("Enter the value  :"))
        dict0.update({key1:value1})
    return (dict0)

def bubble_sort_keys(count, dict1,list1):
    val=0
    list1 = list(dict1.keys())
    print(list1)
    for i in range(count-1):
        if(list1[i]>list1[i+1]):
            val=list1[i]
            list1[i] = list1[i + 1]
            list1[i+1]=val
    print(list1)
    return(list1)



# MAIN Program
count = int(input("Enter the number of elements in the dictionary:  "))
print("Contents of the dictionary ", dict_creation(count,dict1))


print("Bubble Sorted keys of the dictionaries are :  ", bubble_sort_keys(count, dict1, list1))
