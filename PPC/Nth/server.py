import random, sys

msg = '''===== Welcome To Nrd Game =====
Find the nth largest number for me !
----- Example -----
numbers : 1 3 6 12 8 9 13 11
nth : 2
answer > 12
----- Now Your Turn -----
'''

def main():
    print(msg)

    num_list = [random.randint(100, 99999) for i in range(300)]
    nth = random.randint(0, 299)
    print('numbers : ' + ' '.join(str(num) for num in num_list))
    print(f'nth : {nth}')

    input_num = int(input('answer > '))

    num_list.sort()
    if input_num == num_list[-nth]:
        print('SCIST{Rv3o8kX72ozW3ioZbKbyzFVTxlI7PZpL}')
    else:
        print('Wrong Answer')

try:
    main()
except:
    sys.exit()