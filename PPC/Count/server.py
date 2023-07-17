import sys

msg = '''===== Welcome To Counting Game =====
You just need to count from 1 to 100 !
'''

def main():
    print(msg)

    for i in range(100):
        print(f'------ wave {i + 1}/100 ------')
        if int(input()) != (i + 1):
            print('Wrong! You suck!')
            sys.exit()

    print('flag : SCIST{SkQbMFDwrX3NNYEjVfHrXo1Qd0ALzyHi}')

try:
    main()
except:
    sys.exit()