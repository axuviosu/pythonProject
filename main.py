import time
import pyautogui

import time

# Function to simulate typing and pressing enter
def type_message(message):
    for char in message:
        time.sleep(0.05)
        print(char, end='', flush=True)
    time.sleep(0.2)
    print('\n', flush=True)

# Main loop to read chat messages
while True:
    message = input('nerd: ')
    if 'nerd' in message.lower():
        pyautogui.press('enter')
        type_message('nerd')
        pyautogui.press('enter')
# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://bonk.io')
def type_message(message):
    input_field = driver.find_element_by_xpath('//input[@name="message"]')
    input_field.click()
    for char in message:
        time.sleep(0.05)
        input_field.send_keys(char)
    time.sleep(0.2)
    input_field.send_keys('\n')

# Main loop to read chat messages
while True:
    message = input('mom: ')
    if 'nerd' in message.lower():
        pyautogui.press('enter')
        type_message('nerd')
        pyautogui.press('enter')



