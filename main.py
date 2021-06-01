import string
import time
from tqdm import tqdm, trange
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import random
from random import randint
########################
print("""\033[31m
                                                                                  
                                                                                  
                                    ,---,                                    ,-.  
  .--.,    ,---,                  ,--.' |                                ,--/ /|  
,--.'  \ ,---.'|                  |  |  :                              ,--. :/ |  
|  | /\/ |   | :                  :  :  :                              :  : ' /   
:  : :   :   : :                  :  |  |,--.    ,--.--.       ,---.   |  '  /    
:  | |-, :     |,-.               |  :  '   |   /       \     /     \  '  |  :    
|  : :/| |   : '  |               |  |   /' :  .--.  .-. |   /    / '  |  |   \   
|  |  .' |   |  / :               '  :  | | |   \__\/: . .  .    ' /   '  : |. \  
'  : '   '   : |: |          ___  |  |  ' | :   ," .--.; |  '   ; :__  |  | ' \ \ 
|  | |   |   | '/ :       .'  .`| |  :  :_:,'  /  /  ,.  |  '   | '.'| '  : |--'  
|  : \   |   :    |    .'  .'   : |  | ,'     ;  :   .'   \ |   :    : ;  |,'     
|  |,'   /    \  /  ,---, '   .'  `--''       |  ,     .-./  \   \  /  '--'       
`--'     `-'----'   ;   |  .'                  `--`---'       `----'              
                    `---'                                                         

""")
facebook = input (' facebook link :')
print('\033[31m' +'check in ... ')
time.sleep(5)
print('victime found ... ')
time.sleep(3)
print('loading data ... ')
######################################
for i in tqdm([1, 2, 3, 4, 5]):
    time.sleep(0.2)

print('done')

#  special optimised instance of tqdm(range(i))
for i in trange(10):
    time.sleep(0.1)

print('\033[31m' +'done')

# manual: use a with statement
# we can provide the optional 'total' parameter
with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.1)
        pbar.update(10)

print('\033[31m' +'done')

# manual: assign to a variable
# dont forget to call close() at the end
pbar = tqdm(total=100)
for i in range(10):
    time.sleep(0.1)
    pbar.update(10)
pbar.close()
print('\033[31m' +'done')
print('====================================')
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
        files = {
    'email': (None, '{}@gmail.com'.format(username)),
    'password': (None, password),
        }
randsize =randint(8,24)
username=id_generator(randsize)
password=id_generator(randsize)
time.sleep(2)
print("""
 _  _    __     ___  _  __  _   __  _    __     __     __    __  _   ___    
| || |  /  \   / _/ | |/ / | | |  \| |  / _]   | _\   /__\  |  \| | | __|   
| >< | | /\ | | \__ |   <  | | | | ' | | [/\   | v | | \/ | | | ' | | _|    
|_||_| |_||_|  \__/ |_|\_\ |_| |_|\__|  \__/   |__/   \__/  |_|\__| |___|   
""")
time.sleep(2)
print("Email:{}\nPassword:{}".format('{}@gmail.com'.format(username),password))
print('====================================')
print('====================================')
print('ENJOY :)')

