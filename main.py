
# Lucia Jeon
# AID Final Project
# 01/17/2021

"""
before running the code, install the following:
1. Tesseract -> pytesseract
2. openCV
either by Homebrew or Command line tool on mac.
"""

import os
import cv2
import pytesseract
from pytesseract import image_to_string

class Plan:
    def __init__(self, start_time, end_time, name):
        # start_time (float), end_time(float), name(str)
        self.start_time = start_time
        self.end_time = end_time
        self.name = name

plan_count = int(input("How many plans do you have?: "))
plan_list = list()

for i in range(1, plan_count+1):
    start_time = float(input(str(i)+"- start time: "))
    end_time = float(input(str(i)+"- end time: "))
    file_name = input(str(i)+"- image file name: ")
    img=cv2.imread(file_name)
    name = image_to_string(img)
    print(name)
    
    # create a Schedule class instance
    plan_list.append(Plan(start_time, end_time, name))

# evaluate each plans
plan_efficiency = list()
for i in range(plan_count):
    actual_start_time = float(input(str(i+1)+"- actual start time: "))
    actual_end_time = float(input(str(i+1)+"- actual end time: "))
    efficiency = (actual_end_time - actual_start_time) / (plan_list[i].end_time - plan_list[i].start_time)*100
    print("plan", i+1, "efficiency:", efficiency, "%")
    plan_efficiency.append(efficiency)

print("average efficiency:", sum(plan_efficiency)/len(plan_efficiency))
