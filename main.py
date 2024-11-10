import io
import os
import shutil
import sys
import tkinter
import webbrowser
import subprocess
import time
#import PyQt5
#from PyQt5 import QtWidgets, QtGui
from tkinter import messagebox, StringVar, ttk
import datetime
import customtkinter
import customtkinter as ctk
import cv2
import mss
import openpyxl
import pyperclip
import pytz
import pyautogui
from PIL import ImageGrab, Image, ImageFont, ImageDraw, ImageChops, ImageTk
from customtkinter import CTkEntry


def appcore():


    win =ctk.CTk()
    win.geometry("900x600")
    win.resizable (width=False, height=False)
    win.title("Python 3.10 GUI")
    ctk.set_appearance_mode("dark")


    frame1 = ctk.CTkFrame(win)
    frame1.pack(side=ctk. LEFT, pady=20, padx=10)
    frame1.pack_propagate (False)
    frame1.configure (width=180, height=590, border_width=0.7)
    frame2 = ctk.CTkFrame(win)
    frame2.pack(side=ctk. TOP, pady=20, padx=10)
    frame2.pack_propagate (False)
    frame2.configure (width=710, height=85, border_width=0.7)
    framem = ctk.CTkFrame (win)
    framem.pack(side=ctk. BOTTOM, pady=20, padx=20)
    framem.pack_propagate (False)
    framem.configure (width=700,height=420)


    IST= pytz.timezone ('Asia/Kolkata')
    version = 'v1.1'

    def clock():
        #ts1 = datetime.now(IST)
        time.strftime("%d %b %Y")
        time_now = time.strftime("%H:%M:%S %p")
        clocklabel.configure (text=time_now)
        framem.after (1000, clock)
    clocklabel = ctk. CTkLabel (framem, text="", font=("Hrlvetica", 48, "bold"))
    clocklabel.pack()
    clocklabel.place (x=190,y=160)
    clock()



    #A3E4D7 || #F3F2ED, #ECF3F9
    entry = ctk.CTkEntry(frame2, width=660, font =("arial", 48), fg_color="#F3F2ED", corner_radius=12, text_color="black") #A3E4D7 #D1F2EB #760704
    #entry.place(relx-0.5, rely-0.5, anchor-'center')
    entry.place(x=10,y=14) #(padx-30, pady-40)
    #entry.insert(0, "Hi there!")


    globentry= entry.get()
    image=customtkinter.CTkImage(light_image=Image.open("C:\\Images\\PythonGUI.PNG"), size=(90,90))
    image_label= customtkinter.CTkLabel(frame1, image=image, text="")
    image_label.pack()
    image_label.place(x=44,y=20)
    #image.place(x-40,y-15)
    lb =ctk.CTkLabel(frame1, text="Python GUI Tool", font=('arial', 14, "bold"))
    lb.pack()
    lb.place(x=28,y=120)


    def quick_access():
        deleteframe()
        quick_tool=ctk.CTkFrame(framem)
        quick_tool.pack()
        lb = ctk.CTkLabel (quick_tool, text="ONE TOUCH QUICK ACCESS", font =("Helvetica", 15, "bold"))
        lb.pack()
        quick_tool.pack (pady=16,padx=10)



    def browser():
        deleteframe()
        quick_tool=ctk.CTkFrame(framem)
        quick_tool.pack()
        lb = ctk.CTkLabel (quick_tool, text="CROSS BROWSER TESTING", font =("Helvetica", 15, "bold"))
        lb.pack()
        quick_tool.pack (pady=16,padx=10)

        a = ctk.BooleanVar()
        check2 = ctk.CTkCheckBox(framem, text = 'Multi', font =("Helvetica",15))
        check2.pack()
        check2.place(x=60,y=20)





        image2 = customtkinter.CTkImage(light_image = Image.open("C:\\Images\\chrome2.PNG"), size=(90, 80))
        image_label = customtkinter.CTkLabel(framem, image = image2, text="")
        buttonchrome = customtkinter.CTkButton(framem, image = image2, text="", hover_color="red", border_width=0)
        buttonchrome.pack()
        buttonchrome.place(x=60, y=100)  # (x=30,y=180)

        image2 = customtkinter.CTkImage(light_image=Image.open("C:\\Images\\edge.PNG"), size=(90, 80))
        image_label = customtkinter.CTkLabel(framem, image=image2, text="")
        buttonedge = customtkinter.CTkButton(framem, image=image2, text="", hover_color="red", border_width=0)
        buttonedge.pack()
        buttonedge.place(x=250, y=100)  # (x=30,y=180)

        image2 = customtkinter.CTkImage(light_image=Image.open("C:\\Images\\firefox.PNG"), size=(90, 80))
        image_label = customtkinter.CTkLabel(framem, image=image2, text="")
        buttonfirefox = customtkinter.CTkButton(framem, image=image2, text="", hover_color="red", border_width=0)
        buttonfirefox.pack()
        buttonfirefox.place(x=440, y=100)  # (x=30,y=180)



    def links():
        deleteframe()
        quick_tool=ctk.CTkFrame(framem)
        quick_tool.pack()
        lb = ctk.CTkLabel (quick_tool, text="TEST LINKS", font =("Helvetica", 15, "bold"))
        lb.pack()
        quick_tool.pack (pady=16,padx=10)

    def Reports():
        deleteframe()
        quick_tool=ctk.CTkFrame(framem)
        quick_tool.pack()
        lb = ctk.CTkLabel (quick_tool, text="REPORTS", font =("Helvetica", 15, "bold"))
        lb.pack()
        quick_tool.pack (pady=16,padx=10)

    def Testcases():
        deleteframe()
        quick_tool=ctk.CTkFrame(framem)
        quick_tool.pack()
        lb = ctk.CTkLabel (quick_tool, text="TEST CASES", font =("Helvetica", 15, "bold"))
        lb.pack()
        quick_tool.pack (pady=16,padx=10)


    image2= customtkinter.CTkImage(light_image=Image.open("C:\\Images\\Shutdown.PNG"), size=(30,30))
    image_label=customtkinter.CTkLabel (win, image=image2, text="")

    image3 =customtkinter.CTkImage (light_image=Image.open("C:\\Images\\Refresh.PNG"), size=(22,22))
    image_label= customtkinter.CTkLabel (win, image=image3, text="")

    image4=customtkinter.CTkImage(light_image=Image.open("C:\\Images\\Clear.PNG"), size=(22,22))
    image_label= customtkinter.CTkLabel (win, image=image4, text="")

    image5=customtkinter.CTkImage(light_image=Image.open("C:\\Images\\RDP.PNG"), size=(22,22))
    image_label=customtkinter.CTkLabel (win, image=image5, text="")


    image8=customtkinter.CTkImage(light_image=Image.open("C:\\Images\\lock.PNG"), size=(19,19))
    image_label=customtkinter.CTkLabel (win, image=image8, text="")


    buttonturnoff =customtkinter.CTkButton (win, text="",image=image2, height=38,width=40, hover_color="yellow",fg_color="#3e3e42")
    buttonturnoff.place(x=830,y=115)

    buttonrefresh =customtkinter.CTkButton (win, text="",image=image3, height=38,width=40, hover_color="yellow",fg_color="#3e3e42")
    buttonrefresh.place(x=580,y=115)

    buttonclear=customtkinter.CTkButton (win, text="",image=image4, height=38,width=40, hover_color="yellow",fg_color="#3e3e42")
    buttonclear.place(x=450,y=115)


    buttonrdp=customtkinter.CTkButton (win, text="",image=image5, height=38,width=40, hover_color="yellow",fg_color="#3e3e42")
    buttonrdp.place(x=710,y=115)

    buttonlock =customtkinter.CTkButton (win, text="",image=image8, height=38,width=40, hover_color="yellow",fg_color="#3e3e42")
    buttonlock.place(x=340,y=115)









    def deleteframe():
        for frame in framem.winfo_children():
            frame.destroy()



    mode="dark"
    def togglemode():
        global mode
        if mode == "dark":
            ctk.set_appearance_mode("light")
            mode="light"

            buttonturnoff = customtkinter.CTkButton(win, text="", image=image2, height=38, width=40, hover_color="yellow", border_width=1
                                                    )
            buttonturnoff.place(x=830, y=115)

            buttonrefresh = customtkinter.CTkButton(win, text="", image=image3, height=38, width=40, hover_color="yellow",border_width=1
                                                    )
            buttonrefresh.place(x=580, y=115)

            buttonclear = customtkinter.CTkButton(win, text="", image=image4, height=38, width=40, hover_color="yellow",border_width=1
                                    )
            buttonclear.place(x=450, y=115)

            buttonrdp = customtkinter.CTkButton(win, text="", image=image5, height=38, width=40, hover_color="yellow",border_width=1
                                               )
            buttonrdp.place(x=710, y=115)

            buttonlock = customtkinter.CTkButton(win, text="", image=image8, height=38, width=40, hover_color="yellow",border_width=1
                                                 )
            buttonlock.place(x=340, y=115)

        else:
            ctk.set_appearance_mode("dark")
            mode="dark"

            buttonturnoff = customtkinter.CTkButton(win, text="", image=image2, height=38, width=40, hover_color="yellow",
                                                    fg_color="#3e3e42")
            buttonturnoff.place(x=830, y=115)

            buttonrefresh = customtkinter.CTkButton(win, text="", image=image3, height=38, width=40, hover_color="yellow",
                                                    fg_color="#3e3e42")
            buttonrefresh.place(x=580, y=115)

            buttonclear = customtkinter.CTkButton(win, text="", image=image4, height=38, width=40, hover_color="yellow",
                                                  fg_color="#3e3e42")
            buttonclear.place(x=450, y=115)

            buttonrdp = customtkinter.CTkButton(win, text="", image=image5, height=38, width=40, hover_color="yellow",
                                                fg_color="#3e3e42")
            buttonrdp.place(x=710, y=115)

            buttonlock = customtkinter.CTkButton(win, text="", image=image8, height=38, width=40, hover_color="yellow",
                                                 fg_color="#3e3e42")
            buttonlock.place(x=340, y=115)



    mode_switch=ctk.CTkSwitch (win, text="Theme", command=togglemode)
    mode_switch.pack (padx=10, pady=10)
    mode_switch.place(x=225,y=120)





    buttonhome =customtkinter.CTkButton (frame1, text="Quick Access", height=30,width=50, font =("Botthanie", 12), border_width=1, hover_color="green", command=quick_access)
    buttonhome.place(x=40,y=200) #(x-30,y-180)

    buttoncheck =customtkinter.CTkButton(frame1, text="Browsers", height=30,width= 90, font =("Botthanie", 12), border_width=1,hover_color="green",command=browser)
    buttoncheck.place(x=40,y=260) # (x=30,y-180)

    buttonlink =customtkinter.CTkButton(frame1, text="Links", height=30, width =90, font= ("Botthanie", 12), border_width=1, hover_color="green",command=links)
    buttonlink.place(x=40,y=320) #(x-30,y-180)

    buttontesting= customtkinter.CTkButton (frame1, text="Report", height=30,width =90, font =("Botthanie", 12), border_width=1, hover_color="green",command=Reports)
    buttontesting.place(x=40,y=380) #(x-30,y-180)

    buttonwindow =customtkinter.CTkButton(frame1, text="Test Cases", height=30,width= 90, font= ("Botthanie", 12), border_width=1, hover_color="green",command=Testcases)
    buttonwindow.place(x=40,y=448) #(x-38,y-180)

    win.mainloop()

if __name__ == "__main__":
    if "jenkins" in sys.argv:
        print("Running in Jenkins, skipping GUI...")

    else:
        appcore()

