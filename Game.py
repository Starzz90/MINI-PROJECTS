import os
import time
import random

print("Pick a game to play")
print("1.Word Memorize/2.Number Guess")
Pick = int(input("Choose 1/2 : "))
if Pick == 1:
    
# untuk memajukan program: select data/program terus tekan 'tab', dan jika ingin memundurkan data/program tekan "shift+tab"
    def cetak():
        for i in shuffled:
            print(i)

    animal = ["Horse","Duck","Ladybug","Crocodile","Anteater","Cow","Goose","Bunny"]
    print("This is animal memorize")
    print("Your score starts at 100")
    print("and decreases by 10 for every wrong guess")
    Choose = input("Are you ready ?")
    if Choose == "Ready":
        score = 100
        for i in range(3):
            os.system('clear')
            print(i+1)
            Kata = ( i + 2 )*2
            order = random.sample(animal,Kata)
            shuffled = order.copy()
            random.shuffle(shuffled)
            
            for j in order:
                print(j)
            time.sleep(5)
            
            idx = 0
            
            
            while idx < len(order):
                os.system('clear')
                for i in shuffled:
                    print(i)
                jawab = input(f'answer: ,{idx + 1} : ').title()
                if jawab == order[idx]:
                    print('Benar')
                    shuffled.remove(jawab)
                    idx += 1
                else:
                    score -= int(10)
                    print("wrong, try again.")
                    input('(Press enter to continue)')
                     
            os.system('clear')
            input('great , press enter to continue : ')
                
        print('youre score is ',score) 
        cetak()
            
            
if Pick == 2:           



    def menu():
        count = 0
        os.system('clear')
        x = random.randint(0,20)
        print('Welcome to the guessing game')
        print('Guess the number from 0 to 20')
        Pick = input('type in ready if youre ready = ')
        if Pick == "ready":
            while True:
                Y = int(input('type in your number = '))
                if Y < x:
                    print('Number is too low try again')
                    count += 1
                    print('you have tried for', count ,'tries')
                elif Y > x:
                    print('Number is too big try again')
                    count += 1
                    print('you have tried for', count ,'tries')
                elif Y == x:
                    print('Nice your correct')
                    Choice = input("Would you like to go to the next level ? Yes/No =")
                    if Choice == "Yes":
                        count = 0
                        os.system('clear')
                        x = random.randint(0,50)
                        print('Welcome to the guessing game level 2')
                        print('Guess the number from 0 to 50')
                        Pick = input('type in ready if youre ready = ')
                        if Pick == "ready":
                            while True:
                                Y = int(input('type in your number = '))
                                if Y < x:
                                    print('Number is too low try again')
                                    count += 1
                                    print('you have tried for', count ,'tries')
                                elif Y > x:
                                    print('Number is too big try again')
                                    count += 1
    
                    print("oh no you failed")
                    print("the number was",x)
                    count = 0
                    break
        else :
            print("alright press ready if you're ready ")
            menu()    
            
    menu()