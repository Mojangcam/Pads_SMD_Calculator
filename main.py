import os
try:
    from tkinter import *
except:
    os.system('pip install tkinter')
"""

length : foot_size + 1.1
value : row_pitch + 1.4
pin_pitch       pad_width
p < 0.5         0.2
p = 0.5         0.3
p = 0.65        0.35
p = 0.8         0.5
p >= 1.0        0.65

required value
foot_size
row_pitch
pin_pitch

return value
length
row pitch value
pad_width

"""

"""

value
min
max

(min + max) / 2
round

"""

def gui_calc():
    if len(entry1.get()) > 0 and len(entry2.get()) > 0:
        foot_size_min = float(entry1.get())
        foot_size_max = float(entry2.get())
        foot_size = round((foot_size_min + foot_size_max) / 2, 1)
        foot_size_label = Label(tk,text=f"foot size = {foot_size}",fg='black',font=20).grid(row=6,column=0)
        length = round(foot_size + 1.1, 2)
        length_label = Label(tk,text=f"length = {length}",fg='black',font=20).grid(row=7,column=0)
        
    if len(entry3.get()) > 0:
        foot_size = float(entry3.get())
        foot_size_label = Label(tk,text=f"foot size = {foot_size}",fg='black',font=20).grid(row=6,column=0)
        length = round(foot_size + 1.1, 2)
        length_label = Label(tk,text=f"length = {length}",fg='black',font=20).grid(row=7,column=0)
    
    if len(entry4.get()) > 0:
        row_pitch = float(entry4.get())
        row_pitch_value = round(row_pitch + 1.4, 2)
        row_pitch_value_label = Label(tk,text=f"row pitch value = {row_pitch_value}",fg='black',font=20).grid(row=8,column=0)

    if len(entry5.get()) > 0:
        pin_pitch = float(entry5.get())
        if pin_pitch < 0.5:
            pad_width = 0.2
        elif pin_pitch == 0.5:
            pad_width = 0.3
        elif pin_pitch == 0.65:
            pad_width = 0.35
        elif pin_pitch == 0.8:
            pad_width = 0.5
        elif pin_pitch >= 1:
            pad_width = 0.65
        pad_width_label = Label(tk,text=f"pad width = {pad_width}",fg='black',font=20).grid(row=9,column=0)

if __name__ == "__main__":
    tk = Tk()
    tk.title('Pads Helper')
    label1 = Label(tk,text='foot size min').grid(row=0, column=0)
    label2 = Label(tk,text='foot size max').grid(row=1,column=0)
    label3 = Label(tk,text='foot size').grid(row=2,column=0)
    label4 = Label(tk,text='row pitch').grid(row=3,column=0)
    label5 = Label(tk,text='pin pitch').grid(row=4,column=0)
    
    foot_size_label = Label(tk,text="foot size = 0",fg='black',font=20).grid(row=6,column=0)
    length_label = Label(tk,text="length = 0",fg='black',font=20).grid(row=7,column=0)
    row_pitch_value_label = Label(tk,text="row pitch value = 0",fg='black',font=20).grid(row=8,column=0)
    pad_width_label = Label(tk,text="pad width = 0",fg='black',font=20).grid(row=9,column=0)
    
    entry1 = Entry(tk)
    entry2 = Entry(tk)
    entry3 = Entry(tk)
    entry4 = Entry(tk)
    entry5 = Entry(tk)
    
    entry1.grid(row=0,column=1)
    entry2.grid(row=1,column=1)
    entry3.grid(row=2,column=1)
    entry4.grid(row=3,column=1)
    entry5.grid(row=4,column=1)
    
    btn1 = Button(tk,text='계산하기',bg='black',fg='white',command=gui_calc).grid(row=5,column=0)
    tk.mainloop()
