import math
import math as m
Bot: str = 'Sammy'
while True:
        print(f'Hey I am {Bot}, your personal calculator!')
        response: str = input('What would you like to do?').lower().strip()
        try:
            if response in ['+', 'add', 'addition']:
                print(f'Alrighty {Bot} is going to do some {response}!')
                Number1: float = float(input('Enter your first number:'))
                Number2: float = float(input('Enter your second number:'))
                result: float = Number1 + Number2
            elif response in ['-', 'subtract', 'subtraction']:
                print(f'Alrighty {Bot} is going to do some {response}!')
                Number1: float = float(input('Enter your first number:'))
                Number2: float = float(input('Enter your second number:'))
                result: float = Number1 - Number2
            elif response in ['*', 'multiply', 'multiplication']:
                print(f'Alrighty {Bot} is going to do some {response}!')
                Number1: float = float(input('Enter your first number:'))
                Number2: float = float(input('Enter your second number:'))
                result: float = Number1 * Number2
            elif response in ['/', 'divide', 'division']:
                print(f'Alrighty {Bot} is going to do some {response}!')
                Number1: float = float(input('Enter your first number:'))
                Number2: float = float(input('Enter your second number:'))
                result: float = Number1 / Number2
            elif response in ['quit', 'stop', 'break']:
                print(f'Alrighty {Bot} is going to stop! Thank you!')
                break
            else:
                try:
                    print('Please enter a proper command!')
                except ValueError:
                    print(f'Sorry, {Bot} is not a valid option!')
            round_up: str = input('Would you like to round up your answer?').lower().strip()
            if round_up in ['ya', 'yes']:
                far: int = int(input('How much do you want to round-up to:'))
                print(f'Rounding up to {far}!')
                result: float = round(result, far)
                print(f'{result}')
            elif round_up in ['nah', 'no']:
                print(result)
            else:
                print(f'Sorry, {Bot} is not a valid option!')
        except ValueError:
            print('Please enter a proper value!')
