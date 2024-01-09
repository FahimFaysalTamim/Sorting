#print("Hello world")

#Bubbule Sort
new_list=[22,30,21,22,121,1,2,3,4,66]

for step in range (0,len(new_list)-1):

    for index in range(0,len(new_list)-step-1):
       
       if new_list[index] > new_list[index+1] :
           
           temp=new_list[index]
           new_list[index]=new_list[index+1]
           new_list[index+1]=temp

print(f'The final List of Bubble Sort:{new_list}')

#Selection Sort
my_list=[9,12,32,11,3]

for count in range(0,len(my_list)):
    min=my_list[count]
    min_loc=count

    for i in range (count+1, len(my_list)):
        if my_list[i] < min:
            min=my_list[i]
            min_loc=i

    temp=min
    my_list[min_loc]=my_list[count]
    my_list[count]=temp

print("The final List of selection sort :",my_list)

