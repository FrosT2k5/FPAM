import nexmo
from pprint import pprint
import os
import time
import sys



def clr():

  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
clr()


def ban(): 
  banner = """                                         
 ████████  ██████▒     ▒██▒    ███  ███ 
 ████████  ███████▒    ▓██▓    ███  ███ 
 ██        ██   ▒██    ████    ███▒▒███ 
 ███████   ███████▒   ▓█  █▓   ██▒██▒██ 
 ██        ██         ██████   ██ ██ ██ 
 ██        ██        ▒██  ██▒  ██    ██ 
 ██        ██        ███  ███  ██    ██ 
"""
  print(banner)
  
def exit():
  clr()
  ban()
  print('Thanks for using FPAM by FrosT')
  sys.exit()
  
  
ban()


client = nexmo.Client(
  application_id='70cf037f-ee6e-4b58-a381-c8825b980571',
  private_key='files/spammer.key',
)

print('Welcome to FPAM(FrosT Spam) Have Fun :)\n')
i = int(input('Enter the number to be spammed: '))
t = input('Enter the sentence to bo spoken: ')
ncco = [
  { 
    'action': 'talk',
    'timeOut': '1',
    'limit': '1',
    'voiceName': 'Joey',
    'text': t
  }
]


j = int(input('Enter the amount of times to be spammed: '))
k = int(1)

while k <= j:
  clr()
  ban()
  response = client.create_call({
    'to': [{
      'type': 'phone',
      'number': i
    }],
    'from': {
      'type': 'phone',
      'number': '15067160290'
    },
    'ncco': ncco
  })
  pprint(response)
  print('===============')
  print('Spammed',k,'times')
  print('===============')
  k+=1
  time.sleep(1.5)
exit()
  
    
