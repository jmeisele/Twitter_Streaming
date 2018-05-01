#This py file creates an easy to use GUI for streaming and generating a twitter wordcloud based on user search criteria

from tkinter import *
import sys
import os

top = Tk()
l1 = Label(top, text = "What are you wanting to search?")
l1.pack(side = LEFT)

def Twitter_Search():
    os.system('python tweepy_streamer.py')

b1 = Button(top, text = "GO!", command = Twitter_Search)
b1.pack(side = RIGHT)

E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)

top.mainloop()
