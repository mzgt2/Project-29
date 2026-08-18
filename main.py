from tkinter import *
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
flip_timer = None


def next_word():
    global flip_timer, current_card
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    canvas.itemconfig(old_image, image=front_card)
    canvas.itemconfig(language, text="Spanish", fill="black")
    random_row = random.choice(data_dict)
    spanish_word = random_row["Spanish"]

    current_card = random_row
    canvas.itemconfig(text1, text=f"{spanish_word}", fill="black")
    flip_timer = window.after(3000, func=flip_card)

    print(random_row)
    print(current_card)

def right_guess():
    data_dict.remove(current_card)
    pandas.DataFrame(data_dict).to_csv("data/words_to_learn.csv", index=False)
    next_word()
def wrong_guess():
    next_word()

def flip_card():
    canvas.itemconfig(old_image, image=back_card)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(text1, text=current_card["English"], fill="white")


try:
    words_to_learn = pandas.read_csv("data/words_to_learn.csv")
    data_dict = words_to_learn.to_dict(orient="records")

except FileNotFoundError:

    data = pandas.read_csv("data/spanish_words.csv")
    data_dict = data.to_dict(orient="records")


window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
old_image = canvas.create_image(400, 263, image=front_card)
language = canvas.create_text(400,150, text="Spanish", font=("Ariel", 40, "italic"))
text1 = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

back_card = PhotoImage(file="images/card_back.png")


wrong_image = PhotoImage(file="images/wrong.png")
button1 = Button(image=wrong_image, highlightthickness=0, command=wrong_guess)
button1.grid(column=0, row=1)


right_image = PhotoImage(file="images/right.png")
button2 = Button(image=right_image, highlightthickness=0, command=right_guess)
button2.grid(column=1, row=1)


next_word()

window.mainloop()
