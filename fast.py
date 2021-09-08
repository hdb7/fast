from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
import speedtest 

#get the internet speed
def get_speed():
  speed=speedtest.Speedtest()
  download_speed=round((speed.download()/1024)/1024)
  upload_speed=round((speed.upload()/1024)/1024)
  label.config(text='Download Speed: '+str(download_speed)+ 'Mbps'
      +'\n'+'Upload Speed: '+str(upload_speed)+ 'Mbps')

#main UI
style=Style(theme='minty')
window=style.master
window.title('Fast')
window.geometry('600x400')

global label
label=Label(window,text='This is Fast a Simple Internet Speed Checker',
    font=('Helvetica',13)).place(x=100,y=40)
#for styling button
custom_style = ttk.Style()
custom_style.configure('success.Outline.TButton',font=('Helvetica', 12))
button=ttk.Button(window,text='Test', width=10,
    style='success.Outline.TButton',
    command=get_speed).place(x=230,y=150)
window.mainloop()

