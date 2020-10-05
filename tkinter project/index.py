from tkinter import *
window = Tk()
l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISON")
l4.grid(row=1,column=2)

titel_text = StringVar()
el = Entry(window,textvariable = titel_text)
el.grid(row=0,column=1)


auther_text = StringVar()
el = Entry(window,textvariable = auther_text)
el.grid(row=0,column=3)


year_text = StringVar()
el = Entry(window,textvariable = year_text)
el.grid(row=1,column=1)



isbn_text = StringVar()
el = Entry(window,textvariable = isbn_text)
el.grid(row=1,column=3)

list1 = Listbox(window,height = 6,width=35)
list1.grid(row=2,column = 0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=3,column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window,text = "viewall",width = 12)
b1.grid(row=2,column=3)

b2 = Button(window,text = "Search entry",width = 12)
b2.grid(row=3,column=3)

b3 = Button(window,text = "add entry",width = 12)
b3.grid(row=4,column=3)

b4 = Button(window,text = "update selected",width = 12)
b4.grid(row=5,column=3)

b5 = Button(window,text = "delete selected",width = 12)
b5.grid(row=6,column=3)

b6 = Button(window,text = "close",width = 12)
b6.grid(row=7,column=3)

window.mainloop()
