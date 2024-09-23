import tkinter as tk
from tkinter import ttk,messagebox
import json as js
import random as r


class Set_up:
    def __init__(self):
        self.window_setup()
        
    def window_setup(self):
        self.window = tk.Tk()
        self.window.config(padx=50,pady=50,bg = "#fefefe")
        self.window.minsize(height=400,width=600)
        self.window.title("Password Manager")
        self.window.resizable(False,False)
        
    def window_loop(self):
        self.window.mainloop()
        
    def create_labels(self):
        #CREATING LABELS
        self.website_label = tk.Label(text = "Website Name: ")
        self.mail_label = tk.Label(text = "Mail: ")
        self.misc_label = tk.Label(text = "Any other Info : ")
        self.passw_label = tk.Label(text = "Password: ")

        #PLACING LABELS
        self.website_label.grid(row = 2,column=0)
        self.mail_label.grid(row = 4,column=0)
        self.misc_label.grid(row = 5,column=0)
        self.passw_label.grid(row = 3,column=0)

        #EDITING LABELS
        self.website_label.config(bg="#fefefe",padx=5,pady=5,font=("Arial",14))
        self.mail_label.config(bg="#fefefe",padx=5,pady=5,font=("Arial",14))
        self.misc_label.config(bg="#fefefe",padx=5,pady=5,font=("Arial",14))
        self.passw_label.config(bg="#fefefe",padx=5,pady=5,highlightthickness=0,font=("Arial",14))
        
    def adding_canvas(self):
        self.canvas = tk.Canvas(width=400,height=300,highlightthickness=0,borderwidth=0,bg="#fefefe")
        self.lock = tk.PhotoImage(file = "image.png")
        self.canvas.create_image(200,150,image = self.lock)
        self.canvas.grid(row = 0,column=1)
        
    def create_buttons(self):
        #CREATING BUTTONSself.
        self.add = tk.Button(text = "Add Password",command=self.add_clicked)
        self.generate = tk.Button(text= "Genrate",command=self.generate_click)
        self.search = tk.Button(text="Search",command=self.search_clicked)
        self.add_new_mail = tk.Button(text="Add new mail",command=self.add_mail_clicked)

        #PLACING BUTTONS
        self.add.grid(row = 8,column = 1)
        self.generate.grid(row = 3,column=2)
        self.search.grid(row = 2,column=2)
        self.add_new_mail.grid(row=4,column=2)

        #EDITING BUTTONS
        self.add.config(bg="#fefefe",font=("Arial",11),width=25)
        self.generate.config(bg="#fefefe",font=("Arial",11),width=10)
        self.search.config(bg="#fefefe",font=("Arial",11),width=10)
        self.add_new_mail.config(bg="#fefefe",font=("Arial",11),width=10)
        
    def create_entry(self):
        global my_mails
        #CREATING ENTRY BOXES
        self.website_entry = tk.Entry(width = 30)
        self.mail_entry = ttk.Combobox(values=my_mails,width=28)
        self.misc_entry = tk.Entry(width = 30)
        self.passw_entry = tk.Entry(width = 30)

        #PLACING ENTRY BOXES
        self.website_entry.grid(row = 2,column=1,padx = 10,pady = 10)
        self.mail_entry.grid(row = 4,column=1,padx = 10,pady = 10)
        self.passw_entry.grid(row = 3,column=1,padx = 10,pady = 10)
        self.misc_entry.grid(row = 5,column=1,padx = 10,pady = 10)

        #EDITING ENTRY BOXES
        self.website_entry.config(bg="#fefefe",highlightthickness=0.5,font=("Arial",14))
        self.mail_entry.config(background="#fefefe",font=("Arial",14))
        self.misc_entry.config(bg="#fefefe",highlightthickness=0.5,font=("Arial",14))
        self.passw_entry.config(bg="#fefefe",highlightthickness=0.5,font=("Arial",14))
        
    def add_clicked(self):
        self.entered_web = self.website_entry.get().title()
        self.entered_mail = self.mail_entry.get()
        self.entered_passw = self.passw_entry.get()
        self.entered_misc = self.misc_entry.get()
        
        new_dict = {
            self.entered_web: {
                "email" : self.entered_mail,
                "password" : self.entered_passw,
                "Misc" : self.entered_misc
            }
        }
        
        is_ok = (len(self.entered_web) != 0 and len(self.entered_mail) != 0 and len(self.entered_passw) != 0)
        if(is_ok):
            if(messagebox.askokcancel(title = "Confirm?",message = f"Confirm Add?\n{self.entered_web} \n{self.entered_mail} \n{self.entered_passw} \n{self.entered_misc}")):
                try:
                    with open("destination.json",mode = "r") as file:
                        data = js.load(file)
                        data.update(new_dict)
                except FileNotFoundError:
                    with open("destination.json",mode = "w") as file:
                        js.dump(new_dict,file,indent=4)
                else:
                    with open("destination.json",mode = "r") as file:
                        data = js.load(file)
                        data.update(new_dict)
                    with open("destination.json",mode = "w") as file:
                        js.dump(data,file,indent=4)
                finally:
                    print("succesful")
                    self.website_entry.delete(0,"end")
                    self.passw_entry.delete(0,"end")
                    self.misc_entry.delete(0,"end")        
        else:
            messagebox.showinfo(title = "Error", message = "Cant leave a field blank")
    
    def generate_click(self):
        self.passw_entry.delete(0,'end')
        self.entered_web = self.website_entry.get()
        self.entered_web = self.entered_web.title()
        i = r.randint(0,99)
        arr = ['apxfba', 'qcfrclm', 'fsvrim', 'ztipywyje', 'pqmcb', 'cwmjjpny', 'krkuhijck', 'ddrsniftfv', 'oyaxxhvk', 'razhdebl', 'fctajpyf', 'neezrfkbwjg', 'oebtrc', 'nhgqqvlymwz', 'olqisn', 'mswnq', 'kwteugteuojo', 'szafjcta', 'wprmdefzupct', 'cijubbqaglro', 'yknffvg', 'bzhbidnyhcb', 'hwaidrgk', 'vowdpxcs', 'hvbacwzpidk', 'jsycjqturj', 'xldkd', 'wgqnybdhxqtw', 'jcxqfkwuiqvh', 'bwviokvyhtks', 'lxzbexj', 'kgbocdyb', 'khjqf', 'ybmaolqnvdgj', 'gwdqzscfgy', 'pebeqyhgz', 'curisrhzdqn', 'qqhtxwtlsi', 'isjzuhhvdozw', 'icrkayemhiet', 'zyqxyhpe', 'esdffaiss', 'jjauzqm', 'gzwfn', 'ubumgvwloamf', 'czuoadlgy', 'amyfzg', 'wahpdqzkgby', 'mxmnhguzts', 'edepwof', 'impgxuq', 'cpogkicjy', 'neuojowdgrc', 'xcksgtfy', 'zjzgzpusajn', 'wuexjwq', 'eeqcebuglt', 'ruxrcos', 'mygggd', 'mpbeztqxt', 'zsverprsbctx', 'uflxntfhx', 'qudsufjagls', 'qxrryryjro', 'sbgxwccvtkqa', 'hgxuuhdfgz', 'mdfrmabsswim', 'auiczyedm', 'jspwmskzx', 'cimqjvqmqxdh', 'nfbcwlw', 'vmwjp', 'kbnpdqhwnggi', 'bwdwj', 'mbiweatw', 'tvwcf', 'nqegmvrwvz', 'upijz', 'qktar', 'wzkkioszbs', 'rnnztxen', 'efipekrv', 'yyzxihbf', 'kjeczrcvaq', 'sqsraikkh', 'fztahfh', 'bbtlrrqp', 'wiqadqkg', 'dvfyggjvf', 'ghzfeeihrrhn', 'gifiwdpkusq', 'vopdsyj', 'nvjqzifbay', 'tmpqj', 'jbghud', 'fmloyoquepzr', 'waqltgjxra', 'svnenflwuo', 'tlhkj', 'bbhjrxyttgnn']
        temp = r.randint(10000,99999)
        temp2 = f"{self.entered_web}{temp}{arr[i]}"
        self.passw_entry.insert(0,temp2)
        
    def search_clicked(self):
        try:
            file = open("destination.json",mode = "r")
        except:
            messagebox.showinfo(title="File NOT present",message="No passwords are saved yet.")
        else:
            show = "NOT FOUND"
            show1 = "-"
            show2 = "-"
            show3 = "-"
            with open("destination.json",mode = "r") as file:
                searching = js.load(file)
                self.entered_web = self.website_entry.get().title()
                for i in searching:
                    if(self.entered_web == i):
                        show = i
                        show1 = searching[i]["email"]
                        show2 = searching[i]["password"]
                        show3 = searching[i]["Misc"]
                        
                messagebox.showinfo(title="Password",message=f"Website:{show}\nEmail:{show1}\nPassword:{show2}\nMisc:{show3}")
            
    def add_mail_clicked(self):
        with open("Used_mails.txt","a") as file:
            file.write(f"\n{self.mail_entry.get()}")
        with open("Used_mails.txt") as file:
            global my_mails
            my_mails = []
            for i in file.readlines():
                my_mails.append(i)          
        self.mail_entry.config(values=my_mails)
        messagebox.showinfo(title="Added",message="Email added succesfully")
        
with open("Used_mails.txt") as file:
    global my_mails
    my_mails = []
    for i in file.readlines():
        my_mails.append(i)
