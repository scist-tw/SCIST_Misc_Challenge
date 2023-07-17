import random, string, sys

msg = '''===== Welcome To Alphabet Game =====
Count how many English letters there are !
----- Example -----
message : xW_JDb9MMS=p7IP4KD1?I:[+KH)4<<JuyY906544"4AE]I
answer > 23
----- Now Your Turn -----
'''

def count_alphabet(msg):
    count = 0
    for char in msg:
        if char in string.ascii_letters:
            count += 1
    return count

def main():
    print(msg)

    char_list = string.ascii_letters + string.digits + string.punctuation
    for i in range(100):
        message = ''.join(random.choices(char_list, k = random.randint(0x20, 0x30)))
        print(f'------ wave {i + 1}/100 ------')
        print(f'message : {message}')
        if int(input('answer > ')) != count_alphabet(message):
            sys.exit()
    
    print('flag : SCIST{gvfy6KxN3BRMGIMyYlhWjeYRvupJEh8T}')

try:
    main()
except:
    sys.exit()