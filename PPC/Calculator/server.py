import random, sys

msg = '''===== Welcome to the Calculator Game =====
We got some equations here, but the operator is missing. Can you help us?
'''

def main():
    print(msg)

    operator_list = ['+','-','*']
    
    for i in range(100):
        print(f'----- wave {i + 1}/100 -----')
        operator_idx = random.randint(0, 2)
        x, y = random.randint(1, 99), random.randint(1, 99)
        if operator_idx == 0:
            print(f'{x} ? {y} = {x + y}')
        elif operator_idx == 1:
            print(f'{x} ? {y} = {x - y}')
        else:
            print(f'{x} ? {y} = {x * y}')
        if input('which operator (+/-/*) ? ') != operator_list[operator_idx]:
            print('Your math is bad...')
            sys.exit()

    print('flag : SCIST{RPocsDlJBUOeoCSF3fY4UXNACNxmZRTG}')

try:
    main()
except:
    sys.exit()