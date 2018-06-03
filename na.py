from tkinter import *
from newspaper import Article
import socket
import sys
if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk

REMOTE_SERVER = "www.google.com"
def is_connected(hostname):
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(hostname)
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False
x=is_connected(REMOTE_SERVER)
root=Tk(className="News review")
photo=tk.PhotoImage(file="2.gif")
bklab=tk.Label(root, image=photo)
bklab.place(x=0, y=0, relwidth=1, relheight=1)
if x==True:

   y=Label(root,fg="dark green",text="INTERNET ACTIVE")
   y.pack()
   e=Label(root,text="URL")
   e.pack(side=TOP)
   url=StringVar()
   w=Entry(root,textvariable=url)
   w.pack()
   sizex = 8000
   sizey = 6000
   posx  = 1000
   posy  = 1000
   root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
   def call():
        toi_article = Article(url.get(), language="en")
        toi_article.download()
        toi_article.parse()
        toi_article.nlp()
        tex.delete('1.0', END)
        # scrollbar = Scrollbar(root)
        # scrollbar.pack( side = RIGHT, fill=Y )
        # mylist = Listbox(root, yscrollcommand = scrollbar.set )
        # mylist.insert(END,"ARTICLES TITLE")
        # mylist.insert(END,toi_article.title,"\n")
        # mylist.insert(END,"ARTICLES TEXT")
        # mylist.insert(END,toi_article.text,"\n")
        # mylist.insert(END,"ARTICLES SUMMARY")
        # mylist.insert(END,toi_article.summary,"\n")
        # mylist.insert(END,"ARTICLES KEYWORDS")
        # mylist.insert(END,toi_article.keywords,"\n")
        # mylist.pack()
        # scrollbar.config( command = mylist.yview )


        # l=Label(root,text="Articles Title:",font='Helvetica 18 bold')
        # m=Label(root,text=toi_article.title)
        # l.pack()
        # m.pack()
        # n=Label(root,text="Articles Text:",font='Helvetica 18 bold')
        # o=Label(root,text=toi_article.text)
        # n.pack()
        # o.pack()
        # p=Label(root,text="Articles summary:",font='Helvetica 18 bold')
        # q=Label(root,text=toi_article.summary)
        # p.pack()
        # q.pack()
        # r=Label(root,text="Articles keywords:",font='Helvetica 18 bold')
        # s=Label(root,text=toi_article.keywords)
        # r.pack()
        # s.pack()
        tex.insert(tk.END,"ARTICLES TITLE:\n")
        tex.insert(tk.END,toi_article.title+"\n")
        tex.insert(tk.END,"ARTICLES TEXT:\n")
        tex.insert(tk.END,toi_article.text+"\n")
        tex.insert(tk.END,"ARTICLES SUMMARY:\n")
        tex.insert(tk.END,toi_article.summary+"\n")
        tex.insert(tk.END,"ARTICLE KEYWORDS:\n")
        tex.insert(tk.END,toi_article.keywords)
        tex.see(tk.END)



   k=Button(root,text="enter",command=call)
   k.pack()
   tex = tk.Text()
   tex.pack()
   tex.tag_add("start", "1.8", "1.13")
   tex.tag_config("start", background="black", foreground="yellow")

else:
    z=Label(root,fg="red",text="INTERNET NOT ACTIVE")
    z.pack()



root.mainloop()

