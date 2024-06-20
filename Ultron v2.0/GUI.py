from tkinter import*
from PIL import Image, ImageTk
import speech_to_txt
import action
root = Tk()
root.title("Ultron") #title of the frame
root.geometry("550x675") #size of the frame
root.resizable(False, False) #Making the frame sized fixed
root.config(bg="#40E0D0") #bg color

# ask function
def ask():
    ask_val = speech_to_txt.speech_to_txt()
    bot_val = action.Action(ask_val)
    text.insert(END, 'User -----> '+ask_val+"\n")
    if bot_val != None:
        text.insert(END, "BOT <----- "+str(bot_val)+"\n")
    if bot_val == "Oh okay Master" :
        root.destroy()

# send function
def send():
    send = entry.get()
    bot = action.Action(send)
    if bot != None:
        text.insert(END, 'User ---->' +send+"\n")
    if bot == "Oh okay Master" :
        root.destroy()


# delete function
def delete():
    text.delete('1.0', "end")


# frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#40E0D0")
frame.grid(row=0, column=1, padx=55, pady=10)

# text label

text_label = Label(frame, text="Ultron", font=("comic Sans ms", 14, "bold"), bg="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)

# image
image = ImageTk.PhotoImage(Image.open("images/file.png"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

# Text-Widget
text = Text(root, font=('courier 10 bold'), bg="#356696")
text.grid(row=2, column=0)
text.place(x= 100, y=375, width=375, height=100)


# entry widget

entry = Entry(root, justify=CENTER)
entry.place(x=100, y=500, width=350, height=30)

# button 1
Button1 = Button(root, text="Ask", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

# button 2
Button2 = Button(root, text="Send", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400, y=575)

# button 3
Button3 = Button(root, text="Delete", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete)
Button3.place(x=225, y=575)

root.mainloop()