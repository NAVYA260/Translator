from tkinter import *
import googletrans
import textblob
from tkinter import ttk,messagebox
root=Tk('Traslator')
root.geometry("1000x330")
def translate_it():
    pass
def clear():
    #clear the text boxes
    original_text.delete(1.0,END)
    translated_text.delete(1.0,END)

#language_list=(1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,16,1,1,1,1,1,1,1,1,1,1,1,1)

#Grab Language list from googletrans
languages=googletrans.LANGUAGES

language_list=list(languages.values())
print(language_list)
#text boxes
original_text=Text(root,height=10,width=40)
original_text.grid(row=0,column=0,pady=20,padx=10)

translate_button=Button(root,text="TRANSLATE!",font=("Helvetica",24),command=translate_it)
translate_button.grid(row=0,column=1,padx=10)

translated_text=Text(root,height=10,width=40)
translated_text.grid(row=0,column=2,pady=20,padx=10)

#combo boxes
original_combo=ttk.Combobox(root,width=50,value=language_list)
original_combo.current(21)
original_combo.grid(row=1,column=0)

translated_combo=ttk.Combobox(root,width=50,value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1,column=2)
#clear button
clear_button=Button(root,text="clear",command=clear)
clear_button.grid(row=2,column=1)
root.mainloop()