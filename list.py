for i in range(3):
    user_name='srinu'
    pass_word=1234

    user=input('Enter the user_name:')
    password=int(input('Enter the pass_word:'))  
    
    if ((user_name==user) and (pass_word==password)):
        print("login succes")
        amount=10000
        c="credits"       
        w="withrawal"
        m="mini statement"
        type=input('Enter the transaction type:')
        money=int(input('Enter the amount:'))

        if (c==type):
            t=amount + money
            print(t)
            break
        else:
            m=amount-money
            print(m)
            break
    else:
        print('credentials invalid')
        

    result - Enter the user_name:srinu
Enter the pass_word:123
credentials invalid
Enter the user_name:srinu
Enter the pass_word:1234
login succes
Enter the transaction type:credits
Enter the amount:5000
15000



d=[1,3.2,'srinu', True] #
print (d)

result-[1, 3.2, 'srinu', True]


d=[1,3.2,'srinu', True]
print(len(d))
result-4

d=[1,3.2,'srinu', True]
print (d[0:])
result-[1, 3.2, 'srinu', True]

d=[1,3.2,'srinu', True]
print(d[:0])
result-[]

d=[1,3.2,'srinu', True]
print(d[0:2]) #method
result-[1, 3.2]


d=[1,3.2,'srinu', True]
print(d[::-1]) #methof
result - [True, 'srinu', 3.2, 1]

d=[1,3.2,'srinu', True]
d.append(20)
print(d)
result-[1, 3.2, 'srinu', True, 20]



d=[1,3.2,'srinu', True]
d.extend([20,21,4,5,47,])
print(d)

result-[1, 3.2, 'srinu', True, 20, 21, 4, 5, 47]


d=[1,3.2,'srinu', True]
s=d.copy()
d.append(22222)
print(s)

result-[1, 3.2, 'srinu', True]


