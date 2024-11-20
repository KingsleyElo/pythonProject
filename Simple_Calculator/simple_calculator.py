import ast
from tkinter import *

def insert(text):
    entry.insert("end", text)

def clear():
    entry.delete(0, END)

def undo():
    input_current = entry.get()
    if len(input_current):
        clear()
        new = input_current[:-1]
        insert(new)
    else:
        clear()
        new = ""
        insert(new)

def evaluate():
    user_text = entry.get()
    try:
        user_text_eval = ast.parse(user_text, mode = "eval")
        answer = eval(compile(user_text_eval, '<string>', 'eval'))
        clear()
        insert(answer)

    except Exception:
        entry.delete(0, END)
        entry.insert(0, "Invalid Input")
        entry.after(1000, lambda: entry.delete(0, END))

root = Tk()
root.geometry("300x300")
root.title("SIMPLE CALCULATOR")
root.rowconfigure(1,weight=1)
root.columnconfigure(0,weight=1)

entry = Entry(root)
entry.grid(row=0,column=0,sticky="ew", padx=5, pady=5)

content_frame = Frame(root)
content_frame.grid(row=1,column=0, sticky="nsew")
content_frame.rowconfigure((0,1,2,3),weight=1)
content_frame.columnconfigure((0,1,2,3),weight=1)

button_text = [["**2", "*3.14", "**", "+"], [7,8,9,"-"], [4,5,6,"*"], [1,2,3,"/"], ["AC",0,"undo","="]]

for x in range(5):
    for y in range(4):
        text_button = button_text[x][y]
        button = Button(content_frame, text = text_button, command = lambda t = text_button: insert(t), bg="lightgray", width=2, height=2)
        if button.cget("text") == "AC":
            button.config(command = clear)
        if button.cget("text") == "=":
            button.config(command = evaluate)
        if button.cget("text") == "undo":
            button.config(command = undo)
        button.grid(row=x, column=y, sticky="nsew", padx=1, pady=1)

root.mainloop()