#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 16:31:53 2022

@author: carlosdlr
"""

try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter
    
import os

#print(tkinter.TkVersion)
#print(tkinter.TclVersion)

#tkinter._test()

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry("640x480-8-200")
mainWindow['padx'] = 8

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

file_list = tkinter.Listbox(mainWindow)
file_list.grid(row=1, column=0, sticky='nsew', rowspan=2)
file_list.config(border=2, relief='sunken')

for zone in os.listdir('/usr/bin'):
    file_list.insert(tkinter.END, zone)
    
list_scroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=file_list.yview)
list_scroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
file_list['yscrollcommand'] = list_scroll.set


#frame for file explorer
option_frame = tkinter.LabelFrame(mainWindow, text='File Details')
option_frame.grid(row=1, column=2, sticky='ne')

rb_value = tkinter.IntVar()
rb_value.set(3)

# radio buttons
radio_button1 = tkinter.Radiobutton(option_frame, text='Filename', value=1, variable=rb_value)
radio_button2 = tkinter.Radiobutton(option_frame, text='Path', value=2, variable=rb_value)
radio_button3 = tkinter.Radiobutton(option_frame, text='Timestamp', value=3, variable=rb_value)

radio_button1.grid(row=0, column=0, sticky='w')
radio_button2.grid(row=1, column=0, sticky='w')
radio_button3.grid(row=2, column=0, sticky='w')

# label
result_label = tkinter.Label(mainWindow, text='Result')
result_label.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')



# frame for the time spinner
time_frame = tkinter.LabelFrame(mainWindow, text='Time')
time_frame.grid(row=3, column=0, sticky='new')
# time spinners
hour_spinner = tkinter.Spinbox(time_frame, width=2, values=tuple(range(0, 24)))
minute_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
second_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)

hour_spinner.grid(row=0, column=0)
tkinter.Label(time_frame, text=':').grid(row=0, column=1)
minute_spinner.grid(row=0, column=2)
tkinter.Label(time_frame, text=':').grid(row=0, column=3)
second_spinner.grid(row=0, column=4)
time_frame['padx'] = 36


#frame for the date spinners
date_frame = tkinter.LabelFrame(mainWindow)
date_frame.grid(row=4, column=0, sticky='new')

# Date labels
day_label = tkinter.Label(date_frame, text='Day')
month_label = tkinter.Label(date_frame, text='Month')
year_label = tkinter.Label(date_frame, text='Year')

day_label.grid(row=0, column=0, sticky='w')
month_label.grid(row=0, column=1, sticky='w')
year_label.grid(row=0, column=2, sticky='w')

day_spinner = tkinter.Spinbox(date_frame, width=5, from_=1, to=31)
month_spinner = tkinter.Spinbox(date_frame, width=5, values=("Jan","Feb", "Mar", 
                                                             "Apr", "May", "Jun", 
                                                             "Jul", "Aug","Sep",
                                                             "Oct","Nov","Dec"))
year_spinner = tkinter.Spinbox(date_frame, width=5, from_=2000, to=2099)


day_spinner.grid(row=1, column=0)
month_spinner.grid(row=1, column=1)
year_spinner.grid(row=1, column=2)

# Buttons
ok_button = tkinter.Button(mainWindow, text='OK')
cancel_button = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.destroy)

ok_button.grid(row=4, column=3, sticky='e')
cancel_button.grid(row=4, column=4, sticky='w')


















mainWindow.mainloop()

print(rb_value.get())