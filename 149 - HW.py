# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 10:14:21 2023

@author: DELL
"""

from tkinter import*
import random

root = Tk()
root.title("Alphabets")
root.geometry("600x600")
root.configure(background= 'yellow')

letters=["A" , "B" , "C" ,"D" , "E" , "F" , "G" , "H" , "I" , "J" ,"K" , "L" ,  "M" ,"N" , "O", "P" , "Q" , "R", "S", "T" , "U" , "V" , "W" , "X" , "Y" , "Z"]
print(letters)

Label1 = Label(root)

def random_number() :
    random_no1 = random.randint(0,25)
    random_no2 = random.randint(0,25)
    random_no3 = random.randint(0,25)
    random_no4 = random.randint(0,25)
    random_no5 = random.randint(0,25)
    
    random_alpha1 = letters[random_no1]
    random_alpha2 = letters[random_no2]
    random_alpha3 = letters[random_no3]
    random_alpha4 = letters[random_no4]
    random_alpha5 = letters[random_no5]
    
    Label1["text"] = "Your random alphabets are : " + random_alpha1 + random_alpha2 +random_alpha3 +random_alpha4 +random_alpha5
    
    
btn = Button(root, text = "What are your random alphabets?" , command = random_number , bg = "blue" , fg = "white")
btn.place(relx = 0.5 ,rely = 0.5, anchor = CENTER)
Label1.place(relx = 0.5 , rely = 0.6 , anchor = CENTER )

root.mainloop()