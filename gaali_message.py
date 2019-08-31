from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from time import sleep
from tkinter import *
from tkinter import messagebox
from random import choice

gaali = ["chutiye","harami","bhosdk","gandu","lavde","teri gaand maaru","lund k lehsoon","bhadwe","chutmari Ke","chutmari k bhadwe","randwe","machhar ki jaant","gaand k andhe",
            "saale","kutte","teri maa ki","isaa k suar","chhipkali ki gaand","tatto k saudhagar","jaant k baal","chut si shakal k", "randi", "Saali", "Kutiya","tere jese mere tatte khujate h", "land k lehsoon"
            ]
def web_app(phno,msg,num):
        print(phno, type(phno))
        print(msg, type(msg))
        print(num, type(num))
        driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://web.whatsapp.com/")
        ans = messagebox.askyesno("Query","Is Whatsapp Loaded in Browser")
        if ans==True:
                num_ele = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input")
                num_ele.send_keys(phno)
                num_ele.send_keys(Keys.RETURN)
                msg_ele = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
                for i in range(num):
                        msg_ele.send_keys(choice(gaali))
                        msg_ele.send_keys(Keys.RETURN)
        else :
                pass
def numbers(master,f1,phno,msg):
        f1.destroy()
        f2 = Frame(master)
        l1 = Label(f2, text="Enter Number of Message ",bg="lightblue",font=("Arial",10,"bold"))
        l1.grid(row=1,column=1,padx=3,pady=4)
        e1 = Entry(f2,width=30)
        e1.grid(row=1,column=2,padx=4,pady=4,ipadx=4,ipady=4)
        def get_num():
                num = int(e1.get())
                web_app(phno,msg,num)
        b1 = Button(f2, text="Enter", bg="blue",width=6,fg="white",font=("Arial",7,"bold"),command=get_num)
        b1.grid(row=2,column=2,padx=4,pady=4,ipadx=4,ipady=4)
        f2.config(bg="lightblue")
        f2.grid(row=0,column=0,padx=15,pady=60)

def message(master,f1,phno):
        f1.destroy()
        f2 = Frame(master)
        l1 = Label(f2, text="Enter Message to Send ",bg="lightblue",font=("Arial",10,"bold"))
        l1.grid(row=1,column=1,padx=3,pady=4)
        e1 = Entry(f2,width=30)
        e1.grid(row=1,column=2,padx=4,pady=4,ipadx=4,ipady=4)
        def get_msg():
            msg = e1.get()
            numbers(master,f2,phno,msg)    
        b1 = Button(f2, text="Enter", bg="blue",width=6,fg="white",font=("Arial",7,"bold"),command=get_msg)
        b1.grid(row=2,column=2,padx=4,pady=4,ipadx=4,ipady=4)
        f2.config(bg="lightblue")
        f2.grid(row=0,column=0,padx=15,pady=60)

def home(master):
        f2 = Frame(master)
        l1 = Label(f2, text="Enter Phone Number ",bg="lightblue",font=("Arial",10,"bold"))
        l1.grid(row=1,column=1,padx=3,pady=4)
        e1 = Entry(f2,width=30)
        e1.grid(row=1,column=2,padx=4,pady=4,ipadx=4,ipady=4)
        def get_phone():
                phno = int(e1.get())
                message(master,f2,phno)
        b1 = Button(f2, text="Enter", bg="blue",width=6,fg="white",font=("Arial",7,"bold"),command=get_phone)
        b1.grid(row=2,column=2,padx=4,pady=4,ipadx=4,ipady=4)
        f2.config(bg="lightblue")
        f2.grid(row=0,column=0,padx=15,pady=60)
"""def question(master):
        f2 = Frame(master)
        l1 = Label(f2, text="Is Whatsapp Web Loaded ? ",bg="lightblue",font=("Arial",10,"bold"))
        l1.grid(row=2,column=1,padx=3,pady=4)
        b1 = Button(f2, text="Yes", bg="blue",width=6,fg="white",font=("Arial",7,"bold"),command=lambda: home(master,f2))
        b1.grid(row=2,column=2,padx=4,pady=4,ipadx=4,ipady=4)
        b2 = Button(f2, text="No", bg="blue",width=6,fg="white",font=("Arial",7,"bold"),command=lambda : master.quit())
        b2.grid(row=2,column=3,padx=4,pady=4,ipadx=4,ipady=4)
        f2.config(bg="lightblue")
        f2.grid(row=0,column=0,padx=15,pady=60)"""

root = Tk()
home(root)
root.title("Whatsapp Attack")
root.geometry("400x200")
root.config(bg="lightblue")
root.mainloop()
