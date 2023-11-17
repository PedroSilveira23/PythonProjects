import requests
import time 
import schedule 

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '7777777777',
        'message': 'Hello world',
        'key': 'textbelt',
    })
    print(resp.json())
    
    
# schedule.every().day.at('06:00').do(send_message)

schedule.every(5).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    