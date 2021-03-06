'''Create the below pattern using nested for loop in Python.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

#set increment to true
increment = True;

#i denotes no. of stars in each row. initialize it to 1.
i=1;

#Loop until i becomes 0
while i!=0:
    #decrement i when i=5
    if(i==5):
        increment=False;
    #print * in each row for value of i
    for j in range(i):
        print('*', end=' ');
    print();
    
    #increment or decrement based on value of variable increment
    if(increment):
        i=i+1;
    else:
        i=i-1;