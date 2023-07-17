import random, sys

msg = '''===== Welcome To Guess Game =====
Guess the secret number ! Secret number is between 1 and 1073741824 !
'''
secret_num = random.randint(1, 1 << 30)

def main():
    print(msg)
    while True:
        guess_num = int(input('guess > '))
        if guess_num == secret_num:
            print("flag : SCIST{rAuWjzyOlGmDlWx7QPzOkNThbKiBBCvi}")
            sys.exit()
        if guess_num > secret_num:
            print("Too big !")
        else:
            print("Too small !")

try:
    main()
except:
    sys.exit()