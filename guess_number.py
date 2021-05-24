from random import randint 
print('Welcome')
print('I have my number...')
a=randint(1,10)
while True:
    num=input('What\'s your guess [1-10]?')
    Num=int(num)
    if Num>a:
        print('That\'s too high. Try again!')
    elif Num<a:
        print('That\'s too low. Try again!')
    else:
        print('You got it! Thank you for playing!')
        break
    
