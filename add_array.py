def add_array(num):
    arr=[]
    if num <=15:
        for i in range(num):
            i=int(input())
            arr.append(i)
        add=0
        even=0
        for j in arr:
            if j%2 == 0:
                even +=j
            else:
                add +=j
        print("The sum of the even numbers in the array is",add)
        print("The sum of the odd numbers in the array is",even)
    else:
        print("The number accepted only  if less than 15")
    

a=int(input())
add_array(a)
