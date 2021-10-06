from tkinter import *
from PIL import Image, ImageTk
import instaloader

root = Tk()
root.geometry("500x600")
root.configure(background='#000000')
root.resizable(False, False)
root.title("InStalker")

def download_data():
    url = str(link.get())
    instaloader.Instaloader().download_profile(url, profile_pic_only=False)
    Label(root,text="DOWNLOAD COMPLETED",font=("Arial 15"),fg="white",bg="green").place(x=120,y=500)
    Label(root,text="Check Your Current Folder for the downloads",font=("Arial 15"),fg="white",bg="green").place(x=40,y=540)
    

#icon
image_icon = ImageTk.PhotoImage(file="instalker.jpg")
root.iconphoto(False, image_icon)

#logo
logo = Image.open("instalker.jpg")
logo = logo.resize((200, 200), Image.ANTIALIAS)
logo_img = ImageTk.PhotoImage(logo)
Label(image=logo_img).pack(pady=10)

#instagram

link=StringVar()

Label(root,text="Username",bg="#000000",fg="white",font=30).pack(padx=5,pady=25)
link_entry = Entry(root,textvariable=link,width=40,font=18,bd=1).pack(padx=5,pady=5)

Button(root,text="DOWNLOAD DATA",font=('Arial',20,"bold"),bg="lightblue",padx=2,pady=2,command=download_data).pack(padx=5,pady=50)
Label(root,text="Paste anyone's instagram ID in the text box\n and click on Download Data",font=14,fg="white",bg="black").place(x=50,y=340)
Label(root,text="Made By: Mainak",font=("Arial 15"),fg="white",bg="green").place(x=170,y=540)

root.mainloop()