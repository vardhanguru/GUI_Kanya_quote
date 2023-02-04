from tkinter import *
import requests
window=Tk()
window.title("Kanya Quotes App")
# window.config(height=400,width=400)

def get_quote():
    r=requests.get(url='https://api.kanye.rest')
    #r.raise_for_status(0 is used to raise any rest exceptiions
    r.raise_for_status()
    #getting the quote
    quote=r.json()['quote']
    #by using canvas.itemconfig we would change the text displayed.
    canvas.itemconfig(quote_txt,text=quote)

#setting GUI window
window.config(padx=50,pady=50)
canvas=Canvas(width=400,height=400)
bg_image=PhotoImage(file='background.png')
#Backgroung image and having canvas to add images
canvas.create_image(200,200,image=bg_image)

#quote text that is created over canvas have to provide where it should be in the canvas
quote_txt=canvas.create_text(180,180,text="Just Kanya quotes...", width=250, font=("Arial", 15, "bold"), fill="black")
kanye_img = PhotoImage(file="kanye.png")
#button to change quotes
kanye_button = Button(image=kanye_img, highlightthickness=0,command=get_quote)
kanye_button.config(width=100,height=100)
kanye_button.grid(row=2, column=1)

canvas.grid(row=1,column=1)

window.mainloop()

