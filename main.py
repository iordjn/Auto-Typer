import pyautogui
import random
import time

# What you would like to type with out manully typing belongs in string below
writing = "I want to write this"

# Amount of seconds you have before you click on where you would like to time
time.sleep(3)

# Loop to type out each letter one by one with a random gap of 0.1-0.45 seconds between each letter
for char in writing:
    random_interval = random.uniform(0.1, 0.45)
    pyautogui.write(char, interval=random_interval)