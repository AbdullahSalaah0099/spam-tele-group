import requests ,time
from time import sleep
token=input ('\033[;093m》\033[;092mEnter token: ')    
print ()    
groupid=input ('\033[;093m》\033[;092mEnter group ID : ')
print ()
msg=input ('\033[;093m》\033[;092mEnter Message : ')
print ()
while True :
    def sendmsg(message):
        url=f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{groupid}&text={message}'
        t=requests.get (url)
        if t.status_code==200:
            sleep (1)
            print ('\033[;096mDone Send ')
            sleep (1)
        else:
            print ('\033[;091mError')
    sendmsg(msg)
