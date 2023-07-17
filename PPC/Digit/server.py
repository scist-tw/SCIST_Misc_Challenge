import random, sys

digit = [
'''
  ###   
 #   #  
#     # 
#     # 
#     # 
 #   #  
  ###
''',
'''
   #   
  ##   
 # #   
   #   
   #   
   #   
 #####
''',
'''
 #####  
#     # 
      # 
 #####  
#       
#       
#######
''',
'''
 #####  
#     # 
      # 
 #####  
      # 
#     # 
 #####
''',
'''
#       
#    #  
#    #  
#    #  
####### 
     #  
     #
''',
'''
####### 
#       
#       
######  
      # 
#     # 
 #####
''',
'''
 #####  
#     # 
#       
######  
#     # 
#     # 
 #####
''',
'''
####### 
#    #  
    #   
   #    
  #     
  #     
  #
''',
'''
 #####  
#     # 
#     # 
 #####  
#     # 
#     # 
 #####
''',
'''
 #####  
#     # 
#     # 
 ###### 
      # 
#     # 
 #####
'''
]

msg = '''===== Welcome to Digit Game =====
Can you help me recognize some digits?
'''

def main():
    print(msg)

    for i in range(100):
        print(f'----- wave {i + 1}/100 -----')
        num = random.randint(0, 9)
        print(digit[num])
        if int(input('What is this digit? ')) == num:
            print('You are right !')
        else:
            print('No, Your eye is malfunctioned.')
            sys.exit()

    print('flag : SCIST{Wt2aTmFvjXHmhYRQPFm8FoUwkJ6OU3Wn}')

try:
    main()
except:
    sys.exit()