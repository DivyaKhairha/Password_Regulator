import tkinter as tk
from tkinter import messagebox,ttk
import json as js


with open("Used_mails.txt") as file:
    global my_mails
    my_mails = []
    for i in file.readlines():
        my_mails.append(i)
    
def window_setup():
    global window
    window = tk.Tk()
    window.config(padx=50,pady=50,bg = "#fefefe")
    window.minsize(height=400,width=600)
    window.title("Password Manager")
    window.resizable(False,False)

def create_labels():
    global website,mail,misc,passw
    #CREATING LABELS
    website = tk.Label(text = "Website Name: ")
    mail = tk.Label(text = "Mail: ")
    misc = tk.Label(text = "Any other Info : ")
    passw = tk.Label(text = "Password: ")

    #PLACING LABELS
    website.grid(row = 2,column=0)
    mail.grid(row = 4,column=0)
    misc.grid(row = 5,column=0)
    passw.grid(row = 3,column=0)

    #EDITING LABELS
    website.config(bg="#fefefe",padx=5,pady=5,font=("Arial",14))
    mail.config(bg="#fefefe",padx=5,pady=5,font=("Arial",14))
    misc.config(bg="#fefefe",padx=5,pady=5,font=("Arial",14))
    passw.config(bg="#fefefe",padx=5,pady=5,highlightthickness=0,font=("Arial",14))

def adding_canvas():
    global canvas,lock
    canvas = tk.Canvas(width=400,height=300,highlightthickness=0,borderwidth=0,bg="#fefefe")
    lock = tk.PhotoImage(file = "image.png")
    canvas.create_image(200,150,image = lock)
    canvas.grid(row = 0,column=1)

def create_buttons():
    global add,generate,add_new_mail
    #CREATING BUTTONS
    add = tk.Button(text = "Add Password",command=add_clicked)
    generate = tk.Button(text= "Genrate",command=generate_click)
    search = tk.Button(text="Search",command=search_clicked)
    add_new_mail = tk.Button(text="Add new mail",command=add_mail_clicked)

    #PLACING BUTTONS
    add.grid(row = 8,column = 1)
    generate.grid(row = 3,column=2)
    search.grid(row = 2,column=2)
    add_new_mail.grid(row=4,column=2)

    #EDITING BUTTONS
    add.config(bg="#fefefe",font=("Arial",11),width=25)
    generate.config(bg="#fefefe",font=("Arial",11),width=10)
    search.config(bg="#fefefe",font=("Arial",11),width=10)
    add_new_mail.config(bg="#fefefe",font=("Arial",11),width=10)

def create_entry():
    global website1,mail1,misc1,passw1
    #CREATING ENTRY BOXES
    website1 = tk.Entry(width = 30)
    mail1 = ttk.Combobox(values=my_mails,width=28)
    misc1 = tk.Entry(width = 30)
    passw1 = tk.Entry(width = 30)

    #PLACING ENTRY BOXES
    website1.grid(row = 2,column=1,padx = 10,pady = 10)
    mail1.grid(row = 4,column=1,padx = 10,pady = 10)
    passw1.grid(row = 3,column=1,padx = 10,pady = 10)
    misc1.grid(row = 5,column=1,padx = 10,pady = 10)

    #EDITING ENTRY BOXES
    website1.config(bg="#fefefe",highlightthickness=0.5,font=("Arial",14))
    mail1.config(background="#fefefe",font=("Arial",14))
    misc1.config(bg="#fefefe",highlightthickness=0.5,font=("Arial",14))
    passw1.config(bg="#fefefe",highlightthickness=0.5,font=("Arial",14))
    
def add_clicked():
    global e_web,e_mail,e_passw,e_misc
    e_web = website1.get().title()
    e_mail = mail1.get()
    e_passw = passw1.get()
    e_misc = misc1.get()
    
    new_dict = {
        e_web: {
            "email" : e_mail,
            "password" : e_passw,
            "Misc" : e_misc
        }
    }
    
    is_ok = (len(e_web) != 0 and len(e_mail) != 0 and len(e_passw) != 0)
    if(is_ok):
        if(messagebox.askokcancel(title = "Confirm?",message = f"Confirm Add?\n{e_web} \n{e_mail} \n{e_passw} \n{e_misc}")):
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
                website1.delete(0,"end")
                passw1.delete(0,"end")
                misc1.delete(0,"end")
            
                
                
    else:
        messagebox.showinfo(title = "Error", message = "Cant leave a field blank")
    
def generate_click():
    passw1.delete(0,'end')
    e_web = website1.get()
    e_web = e_web.title()
    import random as r
    i = r.randint(0,99)
    arr = ['apxfba', 'qcfrclm', 'fsvrim', 'ztipywyje', 'pqmcb', 'cwmjjpny', 'krkuhijck', 'ddrsniftfv', 'oyaxxhvk', 'razhdebl', 'fctajpyf', 'neezrfkbwjg', 'oebtrc', 'nhgqqvlymwz', 'olqisn', 'mswnq', 'kwteugteuojo', 'szafjcta', 'wprmdefzupct', 'cijubbqaglro', 'yknffvg', 'bzhbidnyhcb', 'hwaidrgk', 'vowdpxcs', 'hvbacwzpidk', 'jsycjqturj', 'xldkd', 'wgqnybdhxqtw', 'jcxqfkwuiqvh', 'bwviokvyhtks', 'lxzbexj', 'kgbocdyb', 'khjqf', 'ybmaolqnvdgj', 'gwdqzscfgy', 'pebeqyhgz', 'curisrhzdqn', 'qqhtxwtlsi', 'isjzuhhvdozw', 'icrkayemhiet', 'zyqxyhpe', 'esdffaiss', 'jjauzqm', 'gzwfn', 'ubumgvwloamf', 'czuoadlgy', 'amyfzg', 'wahpdqzkgby', 'mxmnhguzts', 'edepwof', 'impgxuq', 'cpogkicjy', 'neuojowdgrc', 'xcksgtfy', 'zjzgzpusajn', 'wuexjwq', 'eeqcebuglt', 'ruxrcos', 'mygggd', 'mpbeztqxt', 'zsverprsbctx', 'uflxntfhx', 'qudsufjagls', 'qxrryryjro', 'sbgxwccvtkqa', 'hgxuuhdfgz', 'mdfrmabsswim', 'auiczyedm', 'jspwmskzx', 'cimqjvqmqxdh', 'nfbcwlw', 'vmwjp', 'kbnpdqhwnggi', 'bwdwj', 'mbiweatw', 'tvwcf', 'nqegmvrwvz', 'upijz', 'qktar', 'wzkkioszbs', 'rnnztxen', 'efipekrv', 'yyzxihbf', 'kjeczrcvaq', 'sqsraikkh', 'fztahfh', 'bbtlrrqp', 'wiqadqkg', 'dvfyggjvf', 'ghzfeeihrrhn', 'gifiwdpkusq', 'vopdsyj', 'nvjqzifbay', 'tmpqj', 'jbghud', 'fmloyoquepzr', 'waqltgjxra', 'svnenflwuo', 'tlhkj', 'bbhjrxyttgnn']
    temp = r.randint(10000,99999)
    temp2 = f"{e_web}{temp}{arr[i]}"
    passw1.insert(0,temp2)
    
def search_clicked():
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
            e_web = website1.get().title()
            for i in searching:
                if(e_web == i):
                    show = i
                    show1 = searching[i]["email"]
                    show2 = searching[i]["password"]
                    show3 = searching[i]["Misc"]
                    
            messagebox.showinfo(title="Password",message=f"Website:{show}\nEmail:{show1}\nPassword:{show2}\nMisc:{show3}")
        
def add_mail_clicked():
    with open("Used_mails.txt","a") as file:
        file.write(f"\n{mail1.get()}")
    with open("Used_mails.txt") as file:
        global my_mails
        my_mails = []
        for i in file.readlines():
            my_mails.append(i)
    mail1.config(values=my_mails)
    add_new_mail.config(text="Added")
    window.after()
        
    
window_setup()
create_labels()
create_buttons()
create_entry()
adding_canvas()


website1.focus()




window.mainloop()